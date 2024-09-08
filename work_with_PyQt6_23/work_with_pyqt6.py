"""
Перед начало установите Вертуальное окружение и активируйте его
затем установите эти библиотеки:
pip install requests
pip install pyqt6
pip install pyqt-tools
после тогот как все сделаете можете запускать код:)
"""

import sys
import requests

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My app for parsing data from jsonplaceholder")

        button = QPushButton("Press me if you need data")

        button.clicked.connect(self.respons_site)

        self.setCentralWidget(button)

        self.setFixedSize(QSize(500, 500))

    def respons_site(self):
        url = 'https://jsonplaceholder.typicode.com'
        req = requests.get(url, "headers")

        scr = req.text
        with open("index.html", "w", encoding='utf-8') as file:
            file.write(scr)

        print(scr)
    


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()