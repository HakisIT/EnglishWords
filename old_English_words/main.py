from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
import random

lines = {}

with open('D:\Project\English words\english_words.txt', 'r', encoding="utf8") as file:
    lines = list(map(str.strip, file.readlines()))
    dct = {}
    for i in lines:
        if i != '' and '-' in i:
            splt = i.split(' - ')
            dct.update({splt[0]:splt[1]})
    print()

   

# def application():
#     app = QApplication(sys.argv)
#     window = QMainWindow()
#     window.setWindowTitle('English Words')
#     window.setGeometry(300, 200, 350, 250)
#     main_text = QtWidgets.QLabel(window)
#     main_text.setText('test')
#     main_text.move(150, 100)
#     main_text.adjustSize()

#     btn_next = QtWidgets.QPushButton(window)
#     btn_next.setText("Push Me")
#     btn_next.move(160, 200)
#     # btn_next.clicked.connect(click_next)

#     window.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     application()

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.hello = ["Hallo Welt", "你好，世界", "Hei maailma",
            "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World")
        self.text.setAlignment(QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout()
        self.setFixedSize(QSize(400, 300))
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic)


    def magic(self):
        self.text.setText(random.choice(self.hello))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec_())