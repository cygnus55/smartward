# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import json
from signinwindow import *
from sw_string import *

class Ui_WardWindow(object):
    def window_functions(self,MainWindow):
        try:
            with open('ward.json','r') as obj:
                read=json.load(obj)
                mun_name=read['municipality']
                mun_logo=read['mun_logo']
                if not isEmpty(mun_logo):
                    mun_logo_pixmap=QtGui.QPixmap(mun_logo)
                    self.mun_logo_label.setPixmap(mun_logo_pixmap)
                else:
                    self.mun_logo_label.setText("")
                self.Mun_Name.setText(mun_name)
        except Exception as e:
            print("Ward not registered.",e)

        def on_home_button_clicked():
            self.stackedWidget.setCurrentIndex(0)
        
        def logout():
            #logout<<<go to signinwindow
            print("logout pressed")
            MainWindow.hide()
            self.MainWindow = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.MainWindow)
            self.ui.mun_logo.setEchoMode(0)
            # Application start to run
            self.MainWindow.show()
            
                
        def update_profile():
            #update profile
            print("update profile")
            self.stackedWidget.setCurrentIndex(1)
        
        def change_destination_folder():
            #change destination folder
            print("change destination folder")
            self.stackedWidget.setCurrentIndex(2)
        
        def birth_reg():
            #birth registration
            #new Window-birth reg. form
            print("birth registration")
        
        def death_reg():
            #death registration
            #new Window-death reg. form
            print("death registration")

        def marriage_reg():
            #marriage registration
            #new Window-marriage reg. form
            print("marriage registration") 

        def divorce_reg():
            #divorce registration
            #new Window-divorce reg. form
            print("divorce registration") 

        def migration_reg():
            #migration registration
            #new Window-migration reg. form
            print("migration registration") 

        self.home_button.clicked.connect(on_home_button_clicked)
        
        settings_menu=QtWidgets.QMenu()
        settings_menu.addAction("Update Profile",update_profile)
        settings_menu.addAction("Change Destination Folder",change_destination_folder)
        settings_menu.addAction("Logout",logout)
        self.settings_button.setMenu(settings_menu)
        
        vital_reg_menu=QtWidgets.QMenu()
        vital_reg_menu.addAction("Birth registration",birth_reg)
        vital_reg_menu.addAction("Death registration",death_reg)
        vital_reg_menu.addAction("Marriage registration",marriage_reg)
        vital_reg_menu.addAction("Divorce registration",divorce_reg)
        vital_reg_menu.addAction("Migration registration",migration_reg)
        self.vital_reg_button.setMenu(vital_reg_menu)

    def setupUi(self, WardWindow):
        WardWindow.setObjectName("WardWindow")
        WardWindow.resize(1366, 768)
        WardWindow.setMinimumSize(QtCore.QSize(1366, 768))
        WardWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget = QtWidgets.QWidget(WardWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1346, 748))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1902, 200))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.nepal_gov_logo = QtWidgets.QLabel(self.frame)
        self.nepal_gov_logo.setGeometry(QtCore.QRect(0, 10, 150, 148))
        self.nepal_gov_logo.setStyleSheet("border-image: url(:/pic/logo.png);")
        self.nepal_gov_logo.setText("")
        self.nepal_gov_logo.setObjectName("nepal_gov_logo")
        self.Mun_Name = QtWidgets.QLabel(self.frame)
        self.Mun_Name.setGeometry(QtCore.QRect(185, 30, 616, 81))
        self.Mun_Name.setObjectName("Mun_Name")
        self.home_button = QtWidgets.QPushButton(self.frame)
        self.home_button.setGeometry(QtCore.QRect(10, 170, 75, 23))
        self.home_button.setObjectName("home_button")
        self.settings_button = QtWidgets.QPushButton(self.frame)
        self.settings_button.setGeometry(QtCore.QRect(100, 170, 75, 23))
        self.settings_button.setObjectName("settings_button")
        self.mun_logo_label = QtWidgets.QLabel(self.frame)
        self.mun_logo_label.setGeometry(QtCore.QRect(1170, 10, 150, 148))
        self.mun_logo_label.setObjectName("mun_logo_label")
        self.stackedWidget = QtWidgets.QStackedWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 200, 1906, 856))
        self.stackedWidget.setStyleSheet("QPushButton:hover\n"
"{\n"
"background-color:rgb(248, 244, 255);\n"
"}\n"
"QWidget\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.home_page = QtWidgets.QWidget()
        self.home_page.setObjectName("home_page")
        self.vital_reg_button = QtWidgets.QPushButton(self.home_page)
        self.vital_reg_button.setGeometry(QtCore.QRect(30, 50, 540, 80))
        self.vital_reg_button.setObjectName("vital_reg_button")
        self.citizenship_button = QtWidgets.QPushButton(self.home_page)
        self.citizenship_button.setGeometry(QtCore.QRect(30, 220, 540, 80))
        self.citizenship_button.setObjectName("citizenship_button")
        self.sifarish_button = QtWidgets.QPushButton(self.home_page)
        self.sifarish_button.setGeometry(QtCore.QRect(690, 50, 540, 80))
        self.sifarish_button.setObjectName("sifarish_button")
        self.relation_verify_button = QtWidgets.QPushButton(self.home_page)
        self.relation_verify_button.setGeometry(QtCore.QRect(690, 220, 540, 80))
        self.relation_verify_button.setObjectName("relation_verify_button")
        self.stackedWidget.addWidget(self.home_page)
        self.update_profile_page = QtWidgets.QWidget()
        self.update_profile_page.setObjectName("update_profile_page")
        self.stackedWidget.addWidget(self.update_profile_page)
        self.change_directory_page = QtWidgets.QWidget()
        self.change_directory_page.setObjectName("change_directory_page")
        self.stackedWidget.addWidget(self.change_directory_page)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        WardWindow.setCentralWidget(self.centralwidget)
        self.window_functions(WardWindow)
        self.retranslateUi(WardWindow)
        QtCore.QMetaObject.connectSlotsByName(WardWindow)

    def retranslateUi(self, WardWindow):
        _translate = QtCore.QCoreApplication.translate
        WardWindow.setWindowTitle(_translate("WardWindow", "SmartWard"))
        self.Mun_Name.setText(_translate("WardWindow", "Municipality Name \n"
"Slogan"))
        self.home_button.setText(_translate("WardWindow", "Home"))
        self.settings_button.setText(_translate("WardWindow", "Settings"))
        self.mun_logo_label.setText(_translate("WardWindow", "mun_logo"))
        self.vital_reg_button.setText(_translate("WardWindow", "Vital Registration"))
        self.citizenship_button.setText(_translate("WardWindow", "Citizenship"))
        self.sifarish_button.setText(_translate("WardWindow", "Sifaris"))
        self.relation_verify_button.setText(_translate("WardWindow", "Relationship Verification"))
import sw_rc
