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
        self.setWindowIcon(QtGui.QIcon('UkIcon.png'))
        self.hello = list(dct)
        self.dct = dct
        self.button_next_word = QtWidgets.QPushButton()
        self.button2 = QtWidgets.QPushButton()
        self.button3 = QtWidgets.QPushButton()
        self.text = QtWidgets.QLabel("Hello World")
        self.text.setFont(QFont('Times', 35)) 
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.button_next_word.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightblue;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : silver;"
                             "}"
                             )
        self.button_next_word.setIcon(QtGui.QIcon('right-arrow.png'))
        self.button2.setIcon(QtGui.QIcon('flag-for-united-kingdom.svg'))
        self.button3.setIcon(QtGui.QIcon('flag-for-russia.svg'))
        self.button_next_word.setIconSize(QSize(50,50))
        self.button2.setIconSize(QSize(50,50))
        self.button3.setIconSize(QSize(50,50))
        self.button_next_word.setFixedSize(QSize(60, 50))
        self.button2.setFixedSize(QSize(50, 30))
        self.button3.setFixedSize(QSize(50, 30))
        self.layout = QtWidgets.QVBoxLayout()
        self.setFixedSize(QSize(500, 300))
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button_next_word)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.setLayout(self.layout)
        self.past_word = []
        # привязка функции chose_random_word к кнопке стрелочка вправо
        self.button_next_word.clicked.connect(self.next_random_word)
        self.button3.clicked.connect(self.translate)
        self.button2.clicked.connect(self.previous_word)
        print()

    def next_random_word(self):
        self.rnd_word = random.choice(self.hello)
        self.past_word.append(self.rnd_word)
        self.text.setText(self.rnd_word)
        
    def translate(self):
        self.text.setText(self.dct.get(self.rnd_word))

    def previous_word(self):
        self.text.setText(self.past_word[-1])

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec_())