# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signinwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
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
        self.label_3 = QtWidgets.QLabel(self.signinBox)
        self.label_3.setGeometry(QtCore.QRect(195, 195, 196, 41))
        self.label_3.setStyleSheet("background:transparent;\n"
"color: rgb(223, 101, 21);\n"
"    ")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.wardno = QtWidgets.QLineEdit(self.signinBox)
        self.wardno.setGeometry(QtCore.QRect(405, 270, 141, 31))
        self.wardno.setStyleSheet("background:transparent")
        self.wardno.setObjectName("wardno")
        self.address = QtWidgets.QLineEdit(self.signinBox)
        self.address.setGeometry(QtCore.QRect(30, 315, 351, 31))
        self.address.setStyleSheet("background:transparent")
        self.address.setObjectName("address")
        self.state = QtWidgets.QLineEdit(self.signinBox)
        self.state.setGeometry(QtCore.QRect(405, 315, 141, 31))
        self.state.setObjectName("state")
        self.phoneNo = QtWidgets.QLineEdit(self.signinBox)
        self.phoneNo.setGeometry(QtCore.QRect(30, 360, 351, 31))
        self.phoneNo.setStyleSheet("background:transparent")
        self.phoneNo.setText("")
        self.phoneNo.setObjectName("phoneNo")
        self.email = QtWidgets.QLineEdit(self.signinBox)
        self.email.setGeometry(QtCore.QRect(30, 405, 351, 31))
        self.email.setStyleSheet("background:transparent")
        self.email.setObjectName("email")
        self.mun_logo = QtWidgets.QLineEdit(self.signinBox)
        self.mun_logo.setGeometry(QtCore.QRect(30, 450, 351, 31))
        self.mun_logo.setStyleSheet("background:transparent")
        self.mun_logo.setEchoMode(QtWidgets.QLineEdit.Password)
        self.mun_logo.setObjectName("mun_logo")
        self.password = QtWidgets.QLineEdit(self.signinBox)
        self.password.setGeometry(QtCore.QRect(30, 495, 251, 31))
        self.password.setStyleSheet("background:transparent")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.confirmpassword = QtWidgets.QLineEdit(self.signinBox)
        self.confirmpassword.setGeometry(QtCore.QRect(300, 495, 251, 31))
        self.confirmpassword.setStyleSheet("background:transparent")
        self.confirmpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpassword.setObjectName("confirmpassword")
        self.browse = QtWidgets.QPushButton(self.signinBox)
        self.browse.setGeometry(QtCore.QRect(405, 450, 41, 31))
        self.browse.setStyleSheet("border: 2px solid black;\n"
"border-radius:0px;\n"
"border-image:url(:/pic/browse.png);\n"
"\n"
"")
        self.browse.setText("")
        self.browse.setObjectName("browse")
        self.signup = QtWidgets.QPushButton(self.signinBox)
        self.signup.setGeometry(QtCore.QRect(210, 555, 191, 41))
        self.signup.setStyleSheet("border: 2px solid #8f8f91;\n"
"border-radius: 6px;\n"
"background:blue;\n"
"color:white;\n"
"")
        self.signup.setObjectName("signup")
        self.municipality = QtWidgets.QLineEdit(self.signinBox)
        self.municipality.setGeometry(QtCore.QRect(30, 270, 351, 31))
        self.municipality.setStyleSheet("background:transparent")
        self.municipality.setText("")
        self.municipality.setObjectName("municipality")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.municipality, self.wardno)
        MainWindow.setTabOrder(self.wardno, self.address)
        MainWindow.setTabOrder(self.address, self.state)
        MainWindow.setTabOrder(self.state, self.phoneNo)
        MainWindow.setTabOrder(self.phoneNo, self.email)
        MainWindow.setTabOrder(self.email, self.mun_logo)
        MainWindow.setTabOrder(self.mun_logo, self.browse)
        MainWindow.setTabOrder(self.browse, self.password)
        MainWindow.setTabOrder(self.password, self.confirmpassword)
        MainWindow.setTabOrder(self.confirmpassword, self.signup)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Smartवडा"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">REGISTER NEW WARD</span></p></body></html>"))
        self.wardno.setPlaceholderText(_translate("MainWindow", "Ward No."))
        self.address.setPlaceholderText(_translate("MainWindow", "Address"))
        self.state.setPlaceholderText(_translate("MainWindow", "State"))
        self.phoneNo.setPlaceholderText(_translate("MainWindow", "Phone No"))
        self.email.setPlaceholderText(_translate("MainWindow", "E-mail ID"))
        self.mun_logo.setPlaceholderText(_translate("MainWindow", "Municipality/VDC Logo"))
        self.password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.confirmpassword.setPlaceholderText(_translate("MainWindow", "Re-Type your Password"))
        self.signup.setText(_translate("MainWindow", "Sign Up"))
        self.municipality.setPlaceholderText(_translate("MainWindow", "(Rural) Municipality/(Sub) Metropolitan City"))
import sw_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
