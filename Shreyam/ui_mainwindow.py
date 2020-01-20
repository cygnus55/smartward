# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WardWindow(object):
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
        self.stackedWidget = QtWidgets.QStackedWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 200, 1906, 856))
        self.stackedWidget.setStyleSheet("\n"
"QPushButton:hover\n"
"{\n"
"color:red;\n"
"background-color: rgb(255, 245, 235);\n"
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

        self.retranslateUi(WardWindow)
        QtCore.QMetaObject.connectSlotsByName(WardWindow)

    def retranslateUi(self, WardWindow):
        _translate = QtCore.QCoreApplication.translate
        WardWindow.setWindowTitle(_translate("WardWindow", "MainWindow"))
        self.Mun_Name.setText(_translate("WardWindow", "Municipality Name \n"
"Slogan"))
        self.home_button.setText(_translate("WardWindow", "Home"))
        self.settings_button.setText(_translate("WardWindow", "Settings"))
        self.vital_reg_button.setText(_translate("WardWindow", "Vital Registration"))
        self.citizenship_button.setText(_translate("WardWindow", "Citizenship"))
        self.sifarish_button.setText(_translate("WardWindow", "Sifaris"))
        self.relation_verify_button.setText(_translate("WardWindow", "Relationship Verification"))
import sw_rc
