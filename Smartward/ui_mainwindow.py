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
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 10, 150, 148))
        self.label.setStyleSheet("border-image: url(:/pic/logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.Mun_Name = QtWidgets.QLabel(self.frame)
        self.Mun_Name.setGeometry(QtCore.QRect(160, 30, 641, 81))
        self.Mun_Name.setObjectName("Mun_Name")
        self.home_button = QtWidgets.QPushButton(self.frame)
        self.home_button.setGeometry(QtCore.QRect(10, 170, 75, 23))
        self.home_button.setObjectName("home_button")
        self.setting_button = QtWidgets.QPushButton(self.frame)
        self.setting_button.setGeometry(QtCore.QRect(100, 170, 75, 23))
        self.setting_button.setObjectName("setting_button")
        self.stackedWidget = QtWidgets.QStackedWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 281, 1902, 781))
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.Setting_page = QtWidgets.QWidget()
        self.Setting_page.setObjectName("Setting_page")
        self.stackedWidget.addWidget(self.Setting_page)
        self.HomePage = QtWidgets.QWidget()
        self.HomePage.setObjectName("HomePage")
        self.pushButton = QtWidgets.QPushButton(self.HomePage)
        self.pushButton.setGeometry(QtCore.QRect(30, 50, 540, 80))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.HomePage)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 220, 540, 80))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.HomePage)
        self.pushButton_4.setGeometry(QtCore.QRect(690, 50, 540, 80))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.HomePage)
        self.pushButton_5.setGeometry(QtCore.QRect(690, 220, 540, 80))
        self.pushButton_5.setObjectName("pushButton_5")
        self.stackedWidget.addWidget(self.HomePage)
        self.dropbox = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.dropbox.setGeometry(QtCore.QRect(90, 200, 241, 80))
        self.dropbox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropbox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropbox.setObjectName("dropbox")
        self.updateprofile = QtWidgets.QPushButton(self.dropbox)
        self.updateprofile.setGeometry(QtCore.QRect(0, 10, 141, 23))
        self.updateprofile.setObjectName("updateprofile")
        self.changedir = QtWidgets.QPushButton(self.dropbox)
        self.changedir.setGeometry(QtCore.QRect(0, 40, 181, 31))
        self.changedir.setObjectName("changedir")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        WardWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(WardWindow)
        QtCore.QMetaObject.connectSlotsByName(WardWindow)

    def retranslateUi(self, WardWindow):
        _translate = QtCore.QCoreApplication.translate
        WardWindow.setWindowTitle(_translate("WardWindow", "MainWindow"))
        self.Mun_Name.setText(_translate("WardWindow", "Municipality name \n"
"slogan"))
        self.home_button.setText(_translate("WardWindow", "Home"))
        self.setting_button.setText(_translate("WardWindow", "Settings"))
        self.pushButton.setText(_translate("WardWindow", "Vital Registration"))
        self.pushButton_2.setText(_translate("WardWindow", "Citizenship"))
        self.pushButton_4.setText(_translate("WardWindow", "Sifaris"))
        self.pushButton_5.setText(_translate("WardWindow", "Relationship Verification"))
        self.updateprofile.setText(_translate("WardWindow", "Update profile"))
        self.changedir.setText(_translate("WardWindow", "Change Destination Directory"))
import sw_rc



