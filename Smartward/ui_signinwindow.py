# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signinwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(614, 668)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(1366, 768))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("sw_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.signinBox = QtWidgets.QGroupBox(self.centralWidget)
        self.signinBox.setGeometry(QtCore.QRect(10, 10, 591, 641))
        self.signinBox.setMinimumSize(QtCore.QSize(0, 0))
        self.signinBox.setMaximumSize(QtCore.QSize(1366, 768))
        self.signinBox.setStyleSheet("QLineEdit,QGroupBox,QPushButton{\n"
" background:transparent;\n"
"color: rgb(23, 109, 2);\n"
"      border: 2px solid gray;\n"
"      border-radius: 10px;\n"
"}")
        self.signinBox.setTitle("")
        self.signinBox.setObjectName("signinBox")
        self.sw_logo_ = QtWidgets.QLabel(self.signinBox)
        self.sw_logo_.setGeometry(QtCore.QRect(140, 10, 311, 191))
        self.sw_logo_.setStyleSheet("border:none;\n"
"border-radius:0px;\n"
"border-image:url(:/pic/sw_logo.png)")
        self.sw_logo_.setText("")
        self.sw_logo_.setObjectName("sw_logo_")
        self.signStack = QtWidgets.QStackedWidget(self.signinBox)
        self.signStack.setGeometry(QtCore.QRect(10, 180, 571, 441))
        self.signStack.setMinimumSize(QtCore.QSize(0, 0))
        self.signStack.setMaximumSize(QtCore.QSize(1366, 768))
        self.signStack.setStyleSheet("\n"
"background:transparent;\n"
"")
        self.signStack.setObjectName("signStack")
        self.signupPage = QtWidgets.QWidget()
        self.signupPage.setObjectName("signupPage")
        self.municipality = QtWidgets.QLineEdit(self.signupPage)
        self.municipality.setGeometry(QtCore.QRect(30, 60, 351, 31))
        self.municipality.setStyleSheet("background:transparent")
        self.municipality.setText("")
        self.municipality.setObjectName("municipality")
        self.address = QtWidgets.QLineEdit(self.signupPage)
        self.address.setGeometry(QtCore.QRect(30, 110, 511, 31))
        self.address.setStyleSheet("background:transparent")
        self.address.setObjectName("address")
        self.phoneNo = QtWidgets.QLineEdit(self.signupPage)
        self.phoneNo.setGeometry(QtCore.QRect(30, 160, 351, 31))
        self.phoneNo.setStyleSheet("background:transparent")
        self.phoneNo.setText("")
        self.phoneNo.setObjectName("phoneNo")
        self.email = QtWidgets.QLineEdit(self.signupPage)
        self.email.setGeometry(QtCore.QRect(30, 200, 351, 31))
        self.email.setStyleSheet("background:transparent")
        self.email.setObjectName("email")
        self.wardno = QtWidgets.QLineEdit(self.signupPage)
        self.wardno.setGeometry(QtCore.QRect(400, 60, 141, 31))
        self.wardno.setStyleSheet("background:transparent")
        self.wardno.setObjectName("wardno")
        self.mun_logo = QtWidgets.QLineEdit(self.signupPage)
        self.mun_logo.setGeometry(QtCore.QRect(30, 250, 351, 31))
        self.mun_logo.setStyleSheet("background:transparent")
        self.mun_logo.setEchoMode(QtWidgets.QLineEdit.Password)
        self.mun_logo.setObjectName("mun_logo")
        self.password = QtWidgets.QLineEdit(self.signupPage)
        self.password.setGeometry(QtCore.QRect(30, 300, 251, 31))
        self.password.setStyleSheet("background:transparent")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.confirmpassword = QtWidgets.QLineEdit(self.signupPage)
        self.confirmpassword.setGeometry(QtCore.QRect(300, 300, 251, 31))
        self.confirmpassword.setStyleSheet("background:transparent")
        self.confirmpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpassword.setObjectName("confirmpassword")
        self.signup = QtWidgets.QPushButton(self.signupPage)
        self.signup.setGeometry(QtCore.QRect(200, 370, 191, 41))
        self.signup.setStyleSheet("border: 2px solid #8f8f91;\n"
"border-radius: 6px;\n"
"background:blue;\n"
"color:white;\n"
"")
        self.signup.setObjectName("signup")
        self.signin_2 = QtWidgets.QPushButton(self.signupPage)
        self.signin_2.setGeometry(QtCore.QRect(310, 420, 261, 25))
        self.signin_2.setStyleSheet("border:none;")
        self.signin_2.setObjectName("signin_2")
        self.browse = QtWidgets.QPushButton(self.signupPage)
        self.browse.setGeometry(QtCore.QRect(390, 250, 41, 31))
        self.browse.setStyleSheet("border: 2px solid black;\n"
"border-radius:0px;\n"
"border-image:url(:/pic/browse.png);\n"
"\n"
"")
        self.browse.setText("")
        self.browse.setObjectName("browse")
        self.label_3 = QtWidgets.QLabel(self.signupPage)
        self.label_3.setGeometry(QtCore.QRect(180, 10, 181, 41))
        self.label_3.setStyleSheet("background:transparent;\n"
"color: rgb(223, 101, 21);\n"
"    ")
        self.label_3.setObjectName("label_3")
        self.signStack.addWidget(self.signupPage)
        self.forgetPasswordPage = QtWidgets.QWidget()
        self.forgetPasswordPage.setObjectName("forgetPasswordPage")
        self.label_2 = QtWidgets.QLabel(self.forgetPasswordPage)
        self.label_2.setGeometry(QtCore.QRect(150, 20, 241, 41))
        self.label_2.setStyleSheet("background:transparent;\n"
"color: rgb(223, 101, 21);\n"
"    ")
        self.label_2.setObjectName("label_2")
        self.forgetPasswordStack = QtWidgets.QStackedWidget(self.forgetPasswordPage)
        self.forgetPasswordStack.setGeometry(QtCore.QRect(10, 60, 551, 311))
        self.forgetPasswordStack.setObjectName("forgetPasswordStack")
        self.changePasswordPage = QtWidgets.QWidget()
        self.changePasswordPage.setObjectName("changePasswordPage")
        self.new_password = QtWidgets.QLineEdit(self.changePasswordPage)
        self.new_password.setGeometry(QtCore.QRect(50, 60, 471, 41))
        self.new_password.setStyleSheet("background:transparent;")
        self.new_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_password.setObjectName("new_password")
        self.new_password_2 = QtWidgets.QLineEdit(self.changePasswordPage)
        self.new_password_2.setGeometry(QtCore.QRect(50, 140, 471, 41))
        self.new_password_2.setStyleSheet("background:transparent;")
        self.new_password_2.setText("")
        self.new_password_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_password_2.setObjectName("new_password_2")
        self.changePassword = QtWidgets.QPushButton(self.changePasswordPage)
        self.changePassword.setGeometry(QtCore.QRect(190, 220, 171, 41))
        self.changePassword.setStyleSheet("border: 2px solid #8f8f91;\n"
"border-radius: 6px;\n"
"background:blue;\n"
"color:white;\n"
"")
        self.changePassword.setObjectName("changePassword")
        self.forgetPasswordStack.addWidget(self.changePasswordPage)
        self.emailPage = QtWidgets.QWidget()
        self.emailPage.setObjectName("emailPage")
        self.login_id_2 = QtWidgets.QLineEdit(self.emailPage)
        self.login_id_2.setGeometry(QtCore.QRect(50, 130, 471, 41))
        self.login_id_2.setStyleSheet("background:transparent")
        self.login_id_2.setObjectName("login_id_2")
        self.sendEmail = QtWidgets.QPushButton(self.emailPage)
        self.sendEmail.setGeometry(QtCore.QRect(200, 210, 141, 41))
        self.sendEmail.setStyleSheet("border: 2px solid #8f8f91;\n"
"border-radius: 6px;\n"
"background:blue;\n"
"color:white;\n"
"")
        self.sendEmail.setObjectName("sendEmail")
        self.label = QtWidgets.QLabel(self.emailPage)
        self.label.setGeometry(QtCore.QRect(50, 40, 401, 61))
        self.label.setStyleSheet("background:transparent;\n"
"color: rgb(223, 101, 21);\n"
"    ")
        self.label.setObjectName("label")
        self.forgetPasswordStack.addWidget(self.emailPage)
        self.signin_3 = QtWidgets.QPushButton(self.forgetPasswordPage)
        self.signin_3.setGeometry(QtCore.QRect(420, 390, 121, 25))
        self.signin_3.setStyleSheet("border:none;")
        self.signin_3.setObjectName("signin_3")
        self.forgetPasswordStack.raise_()
        self.label_2.raise_()
        self.signin_3.raise_()
        self.signStack.addWidget(self.forgetPasswordPage)
        self.signinPage = QtWidgets.QWidget()
        self.signinPage.setObjectName("signinPage")
        self.login_id = QtWidgets.QLineEdit(self.signinPage)
        self.login_id.setGeometry(QtCore.QRect(50, 110, 471, 41))
        self.login_id.setStyleSheet("background:transparent")
        self.login_id.setObjectName("login_id")
        self.login_password = QtWidgets.QLineEdit(self.signinPage)
        self.login_password.setGeometry(QtCore.QRect(50, 200, 471, 41))
        self.login_password.setStyleSheet("background:transparent;")
        self.login_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_password.setObjectName("login_password")
        self.signin = QtWidgets.QPushButton(self.signinPage)
        self.signin.setGeometry(QtCore.QRect(170, 290, 211, 41))
        self.signin.setStyleSheet("border: 2px solid #8f8f91;\n"
"border-radius: 6px;\n"
"background:blue;\n"
"color:white;\n"
"")
        self.signin.setObjectName("signin")
        self.forgetPassword = QtWidgets.QPushButton(self.signinPage)
        self.forgetPassword.setGeometry(QtCore.QRect(340, 380, 151, 25))
        self.forgetPassword.setStyleSheet("border:none;")
        self.forgetPassword.setObjectName("forgetPassword")
        self.signup_2 = QtWidgets.QPushButton(self.signinPage)
        self.signup_2.setGeometry(QtCore.QRect(490, 380, 61, 25))
        self.signup_2.setStyleSheet("border:none;\n"
"border-left:50px;\n"
"")
        self.signup_2.setObjectName("signup_2")
        self.label_4 = QtWidgets.QLabel(self.signinPage)
        self.label_4.setGeometry(QtCore.QRect(240, 30, 61, 41))
        self.label_4.setStyleSheet("background:transparent;\n"
"color: rgb(223, 101, 21);\n"
"    ")
        self.label_4.setObjectName("label_4")
        self.signStack.addWidget(self.signinPage)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.signStack.setCurrentIndex(1)
        self.forgetPasswordStack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Smartवडा"))
        self.municipality.setPlaceholderText(_translate("MainWindow", "Municipality/VDC"))
        self.address.setPlaceholderText(_translate("MainWindow", "Address"))
        self.phoneNo.setPlaceholderText(_translate("MainWindow", "Phone No,"))
        self.email.setPlaceholderText(_translate("MainWindow", "E-mail ID"))
        self.wardno.setPlaceholderText(_translate("MainWindow", "Ward No."))
        self.mun_logo.setPlaceholderText(_translate("MainWindow", "Municipality/VDC Logo"))
        self.password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.confirmpassword.setPlaceholderText(_translate("MainWindow", "Re-Type your Password"))
        self.signup.setText(_translate("MainWindow", "Sign Up"))
        self.signin_2.setText(_translate("MainWindow", "Already have account,Sign In Instead"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">REGISTER NEW WARD</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">FORGOTTEN YOUR PASSWORD</span></p></body></html>"))
        self.new_password.setPlaceholderText(_translate("MainWindow", "New Password"))
        self.new_password_2.setPlaceholderText(_translate("MainWindow", "Confirm New Password"))
        self.changePassword.setText(_translate("MainWindow", "Change Password"))
        self.login_id_2.setPlaceholderText(_translate("MainWindow", "Enter email id for your account"))
        self.sendEmail.setText(_translate("MainWindow", "Send E-mail"))
        self.label.setText(_translate("MainWindow", "We would send email to your account to authenicate you.\n"
"Please do as you are said."))
        self.signin_3.setText(_translate("MainWindow", "Sign In Instead"))
        self.login_id.setPlaceholderText(_translate("MainWindow", "Id or Gmail"))
        self.login_password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.signin.setText(_translate("MainWindow", "Sign In"))
        self.forgetPassword.setText(_translate("MainWindow", "Forgot your password"))
        self.signup_2.setText(_translate("MainWindow", "|Sign Up"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">LOGIN</span></p></body></html>"))
import sw_rc
