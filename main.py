from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
import sys
import random

lines = {}



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
        with open('D:\Project\English words\english_words.txt', 'r', encoding="utf8") as file:
            lines = list(map(str.strip, file.readlines()))
            dct = {}
            for i in lines:
                if i != '' and '-' in i:
                    splt = i.split(' - ')
                    dct.update({splt[0]:splt[1]})

        self.setWindowTitle('English Words')
        self.setWindowIcon(QtGui.QIcon('flag.png'))
        self.hello = list(dct)
        self.dct = dct
        self.button1 = QtWidgets.QPushButton()
        self.button2 = QtWidgets.QPushButton()
        self.button3 = QtWidgets.QPushButton()
        self.text = QtWidgets.QLabel("Hello World")
        self.text.setFont(QFont('Times', 40)) 
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.button1.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightblue;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : silver;"
                             "}"
                             )
        self.button2.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightblue;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : silver;"
                             "}"
                             )
        self.button1.setIcon(QtGui.QIcon('right-arrow.png'))
        self.button2.setIcon(QtGui.QIcon('arrow.png'))
        self.button3.setIcon(QtGui.QIcon('repeat.png'))
        self.button1.setFixedSize(QSize(150, 30))
        self.button2.setFixedSize(QSize(150, 30))
        self.layout = QtWidgets.QVBoxLayout()
        self.setFixedSize(QSize(500, 300))
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.setLayout(self.layout)
        # привязка функции chose_random_word к кнопке стрелочка вправо
        self.button1.clicked.connect(self.next_random_word)
        self.button3.clicked.connect(self.translate)

    def next_random_word(self):
        self.rnd_word = random.choice(self.hello)
        self.text.setText(self.rnd_word)
        
    def translate(self):
        self.text.setText(self.dct.get(self.rnd_word))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec_())