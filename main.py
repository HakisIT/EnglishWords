from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTabWidget
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

def select_main():
    mycursor = mydb.cursor()
    mycursor.execute('SELECT id FROM main')
    words = mycursor.fetchall()
    lst_index = []
    for i in words:
        lst_index.append(i[0])
    return lst_index


# подтверждение списка подтверждённых индексов слов
def select_know():
    mycursor = mydb.cursor()
    mycursor.execute('SELECT main_word_id FROM know')
    know_words = mycursor.fetchall()
    lst_know_words = []
    for i in know_words:
        lst_know_words.append(int(i[0]))
    return lst_know_words

def select_irregular_verbs():
    mycursor = mydb.cursor()
    mycursor.execute('SELECT id FROM irregular_verbs')
    irregular_words = mycursor.fetchall()
    lst_irregular_words = []
    for i in irregular_words:
        lst_irregular_words.append(int(i[0]))
    return lst_irregular_words


lst_know = select_know()
lst_main = select_main()
lst_irregular = select_irregular_verbs()

def filtered_lst(x):
    if x in lst_know:
        return False
    else:
        return True
    
res_lst = filter(filtered_lst, lst_main)
res_lst = list(res_lst)

def selection():
    random_id = random.choice(res_lst)
    sql_select_query = """SELECT * FROM main WHERE id = %s"""
    mycursor.execute(sql_select_query, (random_id,))
    word1 = mycursor.fetchall()
    dct = {word1[0][0]:[word1[0][1], word1[0][2], word1[0][3]]}
    return dct

def selection_irregular():
    random_id = random.choice(lst_irregular)
    sql_select_query = """SELECT * FROM irregular_verbs WHERE id = %s"""
    mycursor.execute(sql_select_query, (random_id,))
    word1 = mycursor.fetchall()
    dct_irregular = {word1[0][0]:[word1[0][1], word1[0][2], word1[0][3]]}
    return dct_irregular

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

        dct_irregular = {}
        dct_irregular.update(selection_irregular())

        # main window design
        self.setWindowTitle('English Words')
        self.setWindowIcon(QtGui.QIcon('UkIcon.png'))
        self.setFixedSize(QSize(800, 500))
        self.setStyleSheet("background-color: #dbe9f7;")
        self.tab = QtWidgets.QTabWidget()


        self.widget_flash_words = QWidget()
        self.tab.addTab(self.widget_flash_words, "Random Words")
        self.widget_irregular_verbs = QWidget()
        self.tab.addTab(self.widget_irregular_verbs, "Irregular Verbs")
        self.tab1UI()
        self.tab2UI()

        # layout & widget binding
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tab)
        
        self.setLayout(self.layout)


    def tab1UI(self):
        self.layout = QVBoxLayout()

        # greeting & statistics
        self.text = QtWidgets.QLabel("Hello World")
        self.text.setFont(QFont('Times New Roman', 35))
        self.text.setAlignment(QtCore.Qt.AlignCenter)

        text_stats = QtWidgets.QLabel("Statistics")
        text_stats.setFont(QFont('Times New Roman', 25))
        text_stats.setAlignment(QtCore.Qt.AlignRight)

        self.pass_word = 0
        self.passed_words_count = QLabel(f"Passed words: {self.pass_word}")
        self.passed_words_count.setFont(QFont('Times New Roman', 15))
        self.passed_words_count.setAlignment(QtCore.Qt.AlignRight)

        self.know_word_num = 0
        self.know_words_count = QLabel(f"Memorised words: {self.know_word_num}")
        self.know_words_count.setFont(QFont('Times New Roman', 15))
        self.know_words_count.setAlignment(QtCore.Qt.AlignRight)
        
        # create buttons
        button_ru = QtWidgets.QPushButton()
        button_en = QtWidgets.QPushButton()
        button_cz = QtWidgets.QPushButton()
        button_new_word = QtWidgets.QPushButton()
        button_know = QtWidgets.QPushButton()
        button_next_word = QtWidgets.QPushButton()

        # buttons design
        button_next_word.setStyleSheet("QPushButton"
                       "{"
                       "background-color : white;"
                       "border-radius : 5px"
                       "}"
                       "QPushButton::pressed"
                       "{"
                       "background-color : silver;"
                       "}"
                       )
        button_ru.setStyleSheet("QPushButton"
                             "{"
                             "border-radius : 50px"
                             "}"
                             )
        
        button_en.setStyleSheet("QPushButton"
                             "{"
                             "border-radius : 50px"
                             "}"
                             )
        
        button_cz.setStyleSheet("QPushButton"
                             "{"
                             "border-radius : 50px"
                             "}"
                             )
        
        
        # attaching an icon to buttons
        button_next_word.setIcon(QtGui.QIcon('right-arrow.png'))
        button_en.setIcon(QtGui.QIcon('flag-for-united-kingdom.svg'))
        button_ru.setIcon(QtGui.QIcon('flag-for-russia.svg'))
        button_cz.setIcon(QtGui.QIcon('czech-republic-flag-icon.svg'))
        button_new_word.setIcon(QtGui.QIcon('plus-black-symbol.png'))
        button_know.setIcon(QtGui.QIcon('know_icon.png'))

        # icons size fix
        button_next_word.setIconSize(QSize(50,50))
        button_en.setIconSize(QSize(50,50))
        button_ru.setIconSize(QSize(50,50))
        button_cz.setIconSize(QSize(50,50))
        button_new_word.setIconSize(QSize(30,30))
        button_know.setIconSize(QSize(50,50))

        # buttons size fix
        button_next_word.setFixedSize(QSize(60, 50))
        button_en.setFixedSize(QSize(50, 30))
        button_ru.setFixedSize(QSize(50, 30))
        button_cz.setFixedSize(QSize(50, 30))
        button_new_word.setFixedSize(QSize(50, 50))
        button_know.setFixedSize(QSize(50, 50))

        # layout & widget binding
        self.layout.addWidget(text_stats)
        self.layout.addWidget(self.passed_words_count)
        self.layout.addWidget(self.know_words_count)
        self.layout.addWidget(self.text)
        self.layout.addWidget(button_next_word)
        self.layout.addWidget(button_en)
        self.layout.addWidget(button_ru)
        self.layout.addWidget(button_cz)
        self.layout.addWidget(button_new_word)
        self.layout.addWidget(button_know)

        # create shortcuts action
        shortcut_next_word = QShortcut(QKeySequence('Space'), self)
        shortcut_next_word.activated.connect(self.next_random_word)
        shortcut_en = QShortcut(QKeySequence('1'), self)
        shortcut_en.activated.connect(self.translate_en)
        shortcut_ru = QShortcut(QKeySequence('2'), self)
        shortcut_ru.activated.connect(self.translate_ru)
        shortcut_cz = QShortcut(QKeySequence('3'), self)
        shortcut_cz.activated.connect(self.translate_cz)

        # create mouse click action
        button_next_word.clicked.connect(self.next_random_word)
        button_en.clicked.connect(self.translate_en)
        button_cz.clicked.connect(self.translate_cz)
        button_ru.clicked.connect(self.translate_ru)
        button_new_word.clicked.connect(self.append_new_word_in_database)
        button_know.clicked.connect(self.know_word)

        self.widget_flash_words.setLayout(self.layout)


    def tab2UI(self):
        self.layout = QHBoxLayout()
        self.text_irregular = QtWidgets.QLabel("Hello World")
        self.text_irregular.setFont(QFont('Times New Roman', 35))
        self.text_irregular.setAlignment(QtCore.Qt.AlignCenter)
        button_next_word = QtWidgets.QPushButton()
        button_show_verbs = QtWidgets.QPushButton()
        
        button_next_word.setStyleSheet("QPushButton"
                       "{"
                       "background-color : white;"
                       "border-radius : 5px"
                       "}"
                       "QPushButton::pressed"
                       "{"
                       "background-color : silver;"
                       "}"
                       )
        button_show_verbs.setStyleSheet("QPushButton"
                       "{"
                       "background-color : white;"
                       "border-radius : 5px"
                       "}"
                       "QPushButton::pressed"
                       "{"
                       "background-color : silver;"
                       "}"
                       )
        
        button_next_word.setIcon(QtGui.QIcon('right-arrow.png'))
        button_next_word.setIconSize(QSize(50,50))
        button_next_word.setFixedSize(QSize(60, 50))

        button_show_verbs.setIcon(QtGui.QIcon('eye_icon.png'))
        button_show_verbs.setIconSize(QSize(50,50))
        button_show_verbs.setFixedSize(QSize(60, 50))
        
        self.layout.addWidget(button_next_word)
        self.layout.addWidget(button_show_verbs)
        self.layout.addWidget(self.text_irregular)        

        button_next_word.clicked.connect(self.next_irregular_verb)
        button_show_verbs.clicked.connect(self.show_irregular_verb)
        self.widget_irregular_verbs.setLayout(self.layout)


    def next_random_word(self):
        self.select = selection()
        self.values = list(self.select.values())[0]
        self.text.setText(self.values[0])
        self.pass_word += 1
        self.passed_words_count.setText('Passed words: ' + str(self.pass_word))
    

    def next_irregular_verb(self):
        self.select = selection_irregular()
        self.values = list(self.select.values())[0]
        self.text_irregular.setText(self.values[0])


    def show_irregular_verb(self):
        # self.values = list(self.select.values())[0]
        self.text_irregular.setText(self.values[0]+', '+self.values[1]+', '+self.values[2])


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
        if '/' in dialog.textValue():
            sql_insert_query = """INSERT INTO main (english, russian, chech) 
                                VALUES (%s, %s, %s)"""
            tuple1 = (lst_values[0], lst_values[1], lst_values[2])
            mycursor.execute(sql_insert_query, tuple1)
            mydb.commit()


    def know_word(self):
        self.key = self.select.keys()
        sql_insert = """INSERT INTO know (flag, main_word_id)
                              VALUES (%s ,%s)"""
        selection_index = list(self.key)[0]
        tuple = (1, selection_index)
        res_lst.remove(selection_index)
        mycursor.execute(sql_insert, tuple)
        mydb.commit()
        self.know_word_num += 1
        self.know_words_count.setText('Memorised words: ' + str(self.know_word_num))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec_())