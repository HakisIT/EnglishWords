from PyQt5 import QtWidgets, QtCore, QtGui, uic
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
import sys
import random
import mysql.connector


lines = {}

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12312q',
    port='3306',
    database='english_words',
)

mycursor = mydb.cursor()
mycursor.execute('SELECT english, russian, сzech FROM main')
words = mycursor.fetchall()

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        # with open('D:\Project\English words\english_words.txt', 'r', encoding="utf8") as file:
        #     lines = list(map(str.strip, file.readlines()))
        #     dct = {}
        #     for i in lines:
        #         if i != '' and '-' in i:
        #             splt = i.split(' - ')
        #             dct.update({splt[0]:splt[1]})
        dct = {}
        for i in words:
            dct.update({i[0]:[i[1], i[2]]})

        self.setWindowTitle('English Words')
        self.setWindowIcon(QtGui.QIcon('UkIcon.png'))
        self.hello = list(dct)
        self.dct = dct
        self.button_next_word = QtWidgets.QPushButton()
        self.button_ru = QtWidgets.QPushButton()
        self.button_en = QtWidgets.QPushButton()
        self.button_cz = QtWidgets.QPushButton()
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
        
        self.setStyleSheet("background-color: #0f7531;") 


        self.button_next_word.setIcon(QtGui.QIcon('right-arrow.png'))
        self.button_ru.setIcon(QtGui.QIcon('flag-for-united-kingdom.svg'))
        self.button_en.setIcon(QtGui.QIcon('flag-for-russia.svg'))
        self.button_cz.setIcon(QtGui.QIcon('czech-republic.png'))

        self.button_next_word.setIconSize(QSize(50,50))
        self.button_ru.setIconSize(QSize(50,50))
        self.button_en.setIconSize(QSize(50,50))
        self.button_cz.setIconSize(QSize(50,50))
        self.button_next_word.setFixedSize(QSize(60, 50))
        self.button_ru.setFixedSize(QSize(50, 30))
        self.button_en.setFixedSize(QSize(50, 30))
        self.button_cz.setFixedSize(QSize(50, 30))
        self.layout = QtWidgets.QVBoxLayout()
        self.setFixedSize(QSize(500, 300))
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button_next_word)
        self.layout.addWidget(self.button_ru)
        self.layout.addWidget(self.button_en)
        self.layout.addWidget(self.button_cz)
        self.setLayout(self.layout)
        self.past_word = []
        # привязка функции chose_random_word к кнопке стрелочка вправо
        self.button_next_word.clicked.connect(self.next_random_word)
        self.button_en.clicked.connect(self.translate_en)
        self.button_cz.clicked.connect(self.translate_cz)
        self.button_ru.clicked.connect(self.translate_ru)


    def next_random_word(self):
        self.rnd_word = random.choice(self.hello)
        self.past_word.append(self.rnd_word)
        self.text.setText(self.rnd_word)
        
    def translate_en(self):
        self.text.setText(self.dct.get(self.rnd_word)[0])

    def translate_cz(self):
        self.text.setText(self.dct.get(self.rnd_word)[1])

    def translate_ru(self):
        self.text.setText(self.past_word[-1])

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec_())