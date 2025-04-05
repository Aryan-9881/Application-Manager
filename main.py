from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
import sys
import subprocess

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Application Manager")
        self.setGeometry(300, 300, 600, 500)
        self.setWindowIcon(QIcon(r"C:\Users\dell\Pictures\Captain_America_Shield.webp"))  # Replace with your icon path
        self.setStyleSheet("background-color: #1e1e2f; color: white;")

        layout = QVBoxLayout()

        # Welcome Label
        label = QLabel("Welcome to Your Application Manager", self)
        label.setFont(QFont("Arial", 18, QFont.Bold))
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("color: #ff79c6; margin-bottom: 20px;")
        layout.addWidget(label)

        # Buttons with style
        buttons = {
            "Open VS Code": self.open_vscode,
            "Open YouTube": self.open_youtube,
            "Open ChatGPT": self.open_chatgpt,
            "Open All": self.open_all
        }

        for btn_text, btn_function in buttons.items():
            button = QPushButton(btn_text)
            button.clicked.connect(btn_function)
            button.setFont(QFont("Arial", 12))
            button.setStyleSheet("""
                QPushButton {
                    background-color: #6272a4;
                    color: white;
                    padding: 12px;
                    border-radius: 10px;
                }
                QPushButton:hover {
                    background-color: #7085d8;
                }
            """)
            layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_vscode(self):
        subprocess.Popen([r"C:\Users\dell\AppData\Local\Programs\Microsoft VS Code\Code.exe"])

    def open_youtube(self):
        subprocess.Popen(["start", "chrome", "https://www.youtube.com"], shell=True)

    def open_chatgpt(self):
        subprocess.Popen(["start", "chrome", "https://chat.openai.com"], shell=True)

    def open_all(self):
        self.open_vscode()
        self.open_youtube()
        self.open_chatgpt()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
