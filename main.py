from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtWidgets import QMessageBox
import sys
import random
import mysql.connector
import ctypes


lines = {}

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12312q',
    port='3306',
    database='english_words',
)

mycursor = mydb.cursor()
mycursor.execute('SELECT id FROM main')
words = mycursor.fetchall()
lst_index = []
for i in words:
    lst_index.append(i[0])

def selection():
    random_id = random.choice(lst_index)
    sql_select_query = """SELECT * FROM main WHERE id = %s"""
    mycursor.execute(sql_select_query, (random_id,))
    word1 = mycursor.fetchall()
    dct = {word1[0][0]:[word1[0][1], word1[0][2], word1[0][3]]}
    return dct

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        # work with txt file
        # with open('D:\Project\English words\english_words.txt', 'r', encoding="utf8") as file:
        #     lines = list(map(str.strip, file.readlines()))
        #     dct = {}
        #     for i in lines:
        #         if i != '' and '-' in i:
        #             splt = i.split(' - ')
        #             dct.update({splt[0]:splt[1]})

        dct = {}
        dct.update(selection())
        self.setWindowTitle('English Words')
        self.setWindowIcon(QtGui.QIcon('UkIcon.png'))
        self.button_next_word = QPushButton()
        self.button_ru = QtWidgets.QPushButton()
        self.button_en = QtWidgets.QPushButton()
        self.button_cz = QtWidgets.QPushButton()
        self.button_new_word = QtWidgets.QPushButton()
        # self.button_shortcut_show = QtWidgets.QPushButton()
        self.text = QtWidgets.QLabel("Hello World")
        self.text.setFont(QFont('Times New Roman', 35))
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.button_next_word.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightblue;"
                             "border-radius : 5px"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : silver;"
                             "}"
                             )
        
        self.button_ru.setStyleSheet("QPushButton"
                             "{"
                             "border-radius : 50px"
                             "}"
                             )
        
        self.button_en.setStyleSheet("QPushButton"
                             "{"
                             "border-radius : 50px"
                             "}"
                             )
        
        self.button_cz.setStyleSheet("QPushButton"
                             "{"
                             "border-radius : 50px"
                             "}"
                             )

        self.setStyleSheet("background-color: #0f7531;") 
        self.button_next_word.setIcon(QtGui.QIcon('right-arrow.png'))
        self.button_en.setIcon(QtGui.QIcon('flag-for-united-kingdom.svg'))
        self.button_ru.setIcon(QtGui.QIcon('flag-for-russia.svg'))
        self.button_cz.setIcon(QtGui.QIcon('czech-republic-flag-icon.svg'))
        self.button_new_word.setIcon(QtGui.QIcon('plus-black-symbol.png'))
        # self.button_shortcut_show.setIcon(QtGui.QIcon('shortcut-script-app.png'))
        self.button_next_word.setIconSize(QSize(50,50))
        self.button_en.setIconSize(QSize(50,50))
        self.button_ru.setIconSize(QSize(50,50))
        self.button_cz.setIconSize(QSize(50,50))
        self.button_new_word.setIconSize(QSize(30,30))
        # self.button_shortcut_show.setIconSize(QSize(50,50))
        self.button_next_word.setFixedSize(QSize(60, 50))
        self.button_en.setFixedSize(QSize(50, 30))
        self.button_ru.setFixedSize(QSize(50, 30))
        self.button_cz.setFixedSize(QSize(50, 30))
        self.button_new_word.setFixedSize(QSize(50, 50))
        # self.button_shortcut_show.setFixedSize(QSize(55, 55))
        self.layout = QtWidgets.QVBoxLayout()
        # self.layout = QtWidgets.QGridLayout()

        # self.layout.resize(120, 80)
        self.setFixedSize(QSize(500, 300))
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button_next_word)
        self.layout.addWidget(self.button_en)
        self.layout.addWidget(self.button_ru)
        self.layout.addWidget(self.button_cz)
        self.layout.addWidget(self.button_new_word)
        # self.layout.addWidget(self.button_shortcut_show)
        self.setLayout(self.layout)
        self.past_word = []
        # create shortcut's action
        self.shortcut_next_word = QShortcut(QKeySequence('Space'), self)
        self.shortcut_next_word.activated.connect(self.next_random_word)
        self.shortcut_en = QShortcut(QKeySequence('1'), self)
        self.shortcut_en.activated.connect(self.translate_en)
        self.shortcut_ru = QShortcut(QKeySequence('2'), self)
        self.shortcut_ru.activated.connect(self.translate_ru)
        self.shortcut_cz = QShortcut(QKeySequence('3'), self)
        self.shortcut_cz.activated.connect(self.translate_cz)
        # create mouse click action
        self.button_next_word.clicked.connect(self.next_random_word)
        self.button_en.clicked.connect(self.translate_en)
        self.button_cz.clicked.connect(self.translate_cz)
        self.button_ru.clicked.connect(self.translate_ru)
        self.button_new_word.clicked.connect(self.append_new_word_in_database)


    def next_random_word(self):
        self.select = selection()
        self.values = list(self.select.values())[0]
        self.text.setText(self.values[0])

    def translate_cz(self):
        self.text.setText(self.values[2])


    def translate_ru(self):
        self.text.setText(self.values[1])

    def translate_en(self):
        self.text.setText(self.values[0])

    def append_new_word_in_database(self):
        dialog = QInputDialog()
        dialog.setLabelText('Eng/Ru/Cz word translation')
        dialog.exec()
        lst_values = dialog.textValue().split('/')
        # sql_select_query = "INSERT INTO `english_words` (`'id'`, `'english'`, `'russian'`, `'czech'`) VALUES ({0}, {1}, {2}, {3}".format(172, lst_values[0], lst_values[1], lst_values[2])
        # mycursor.execute(sql_select_query)
        # mycursor.execute(sql_select_query, (lst_values[0], lst_values[1], lst_values[2]))
        # mycursor.execute("INSERT INTO main (english, russian, chech) VALUES ({}, {}, {})".format(lst_values[0], lst_values[1], lst_values[2]))
        sql_insert_query = """INSERT INTO main (english, russian, chech) 
                              VALUES (%s, %s, %s)"""
        
        tuple1 = (lst_values[0], lst_values[1], lst_values[2])
        mycursor.execute(sql_insert_query, tuple1)
        mydb.commit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec_())