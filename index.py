from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


import sys


from PyQt5.uic import loadUiType

ui, _ = loadUiType('library.ui')


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI_Changes()
        self.Handel_Buttons()

    def Handel_UI_Changes(self):
        self.Hiding_Themes()
        self.tabWidget.tabBar().setVisible(False)

    def Handel_Buttons(self):
        self.pushButton_5.clicked.connect(self.Show_Themes)
        self.pushButton_21.clicked.connect(self.Hiding_Themes)

        self.pushButton.clicked.connect(self.Open_day_tab)
        self.pushButton_4.clicked.connect(self.Open_book_tab)
        self.pushButton_2.clicked.connect(self.Open_user_tab)
        self.pushButton_3.clicked.connect(self.Open_setting_tab)

        self.pushButton_7.clicked.connect(self.Add_new_Book)

        self.pushButton_20.clicked.connect(self.Add_Category)

    def Show_Themes(self):
        self.groupBox_3.show()

    def Hiding_Themes(self):
        self.groupBox_3.hide()

        ##### open Tabas ###

    def Open_day_tab(self):
        self.tabWidget.setCurrentIndex(0)

    def Open_book_tab(self):

        self.tabWidget.setCurrentIndex(1)

    def Open_user_tab(self):
        self.tabWidget.setCurrentIndex(2)

    def Open_setting_tab(self):
        self.tabWidget.setCurrentIndex(3)

#### Books###

    def Add_new_Book(self):

        self.db = MySQLdb.connect(
            host='localhost', user='root', password='@isse123', db='library')

        self.cur = self.db.cursor()

        book_title = self.lineEdit_3.text()
        book_code = self.lineEdit_4.text()
        book_category = self.comboBox_3.currentText()
        book_publisher = self.comboBox_5.currentText()
        book_price = self.lineEdit_5.text()

    def Search_Book(self):
        pass

    def Edit_Book(self):
        pass

    def Delete_Book(self):
        pass

    ##########Users#############

    def Add_New_User(self):
        pass

    def Login(self):
        pass

    def Edit_User(self):
        pass

    ########## Settings #############

    def Add_Category(self):
        self.db = MySQLdb.connect(
            host='localhost', user='root', password='@isse123')

        self.cur = self.db.cursor()

        category_name = self.lineEdit_34.text()

        self.cursor.execute('''
           INSERT INTO category (name) VALUES = (%s)
        
        ''', (category_name))

        self.db.connect()
        print('done')

        pass

    def Add_Author(self):

        pass

    def Add_Publisher():
        pass


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


main()
