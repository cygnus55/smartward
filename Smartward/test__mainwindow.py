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
        self.frame.setStyleSheet("QFrame\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgb(248, 244, 255);\n"
"}\n"
"QPushButton\n"
"{\n"
"font-size:16px;\n"
"}\n"
"QLabel\n"
"{\n"
"color:red;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.nepal_gov_logo = QtWidgets.QLabel(self.frame)
        self.nepal_gov_logo.setGeometry(QtCore.QRect(0, 10, 150, 148))
        self.nepal_gov_logo.setStyleSheet("border-image: url(:/pic/logo.png);")
        self.nepal_gov_logo.setText("")
        self.nepal_gov_logo.setObjectName("nepal_gov_logo")
        self.Mun_Name = QtWidgets.QLabel(self.frame)
        self.Mun_Name.setGeometry(QtCore.QRect(185, 30, 616, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Mun_Name.setFont(font)
        self.Mun_Name.setStyleSheet("")
        self.Mun_Name.setText("")
        self.Mun_Name.setObjectName("Mun_Name")
        self.home_button = QtWidgets.QPushButton(self.frame)
        self.home_button.setGeometry(QtCore.QRect(10, 163, 121, 30))
        self.home_button.setStyleSheet("border-radius:6px;\n"
"border:1px solid rgb(170, 170, 127);\n"
"qproperty-icon:url(:pic/home-icon.png);\n"
"")
        self.home_button.setObjectName("home_button")
        self.settings_button = QtWidgets.QPushButton(self.frame)
        self.settings_button.setGeometry(QtCore.QRect(135, 163, 136, 30))
        self.settings_button.setStyleSheet("border-radius:6px;\n"
"border:1px solid rgb(170, 170, 127);\n"
"qproperty-icon:url(:pic/settings-icon.png);")
        self.settings_button.setObjectName("settings_button")
        self.mun_logo_label = QtWidgets.QLabel(self.frame)
        self.mun_logo_label.setGeometry(QtCore.QRect(1170, 10, 150, 148))
        self.mun_logo_label.setText("")
        self.mun_logo_label.setObjectName("mun_logo_label")
        self.Mun_Ward_num = QtWidgets.QLabel(self.frame)
        self.Mun_Ward_num.setGeometry(QtCore.QRect(185, 60, 600, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Mun_Ward_num.setFont(font)
        self.Mun_Ward_num.setStyleSheet("")
        self.Mun_Ward_num.setText("")
        self.Mun_Ward_num.setObjectName("Mun_Ward_num")
        self.stackedWidget = QtWidgets.QStackedWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 200, 1366, 568))
        self.stackedWidget.setStyleSheet("QPushButton:hover\n"
"{\n"
"background-color:rgb(248, 244, 255);\n"
"}\n"
"QPushButton#delete_account_button:hover{\n"
"background-color:rgb(255, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton#change_password_button:hover{\n"
"background-color: rgb(170, 170, 255);\n"
"color:rgb(0, 0, 127);\n"
"}\n"
"QPushButton#delete_account_button\n"
"{\n"
"background-color:rgb(248, 244, 255);\n"
"}\n"
"QPushButton#change_password_button\n"
"{\n"
"background-color:rgb(248, 244, 255);\n"
"}\n"
"QPushButton{\n"
"border-radius:10px;\n"
"border:1px solid rgb(170, 170, 127);\n"
"font-size:16px;\n"
"}\n"
"QWidget\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.home_page = QtWidgets.QWidget()
        self.home_page.setObjectName("home_page")
        self.vital_reg_button = QtWidgets.QPushButton(self.home_page)
        self.vital_reg_button.setGeometry(QtCore.QRect(30, 75, 540, 91))
        self.vital_reg_button.setStyleSheet("")
        self.vital_reg_button.setObjectName("vital_reg_button")
        self.citizenship_button = QtWidgets.QPushButton(self.home_page)
        self.citizenship_button.setGeometry(QtCore.QRect(30, 220, 540, 91))
        self.citizenship_button.setObjectName("citizenship_button")
        self.sifarish_button = QtWidgets.QPushButton(self.home_page)
        self.sifarish_button.setGeometry(QtCore.QRect(690, 75, 540, 91))
        self.sifarish_button.setObjectName("sifarish_button")
        self.relation_verify_button = QtWidgets.QPushButton(self.home_page)
        self.relation_verify_button.setGeometry(QtCore.QRect(690, 220, 540, 91))
        self.relation_verify_button.setObjectName("relation_verify_button")
        self.statistics_button = QtWidgets.QPushButton(self.home_page)
        self.statistics_button.setGeometry(QtCore.QRect(30, 375, 540, 91))
        self.statistics_button.setObjectName("statistics_button")
        self.stackedWidget.addWidget(self.home_page)
        self.change_password = QtWidgets.QWidget()
        self.change_password.setObjectName("change_password")
        self.groupBox = QtWidgets.QGroupBox(self.change_password)
        self.groupBox.setGeometry(QtCore.QRect(180, 90, 496, 256))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.old_password_lineedit = QtWidgets.QLineEdit(self.groupBox)
        self.old_password_lineedit.setGeometry(QtCore.QRect(75, 45, 256, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.old_password_lineedit.setFont(font)
        self.old_password_lineedit.setStyleSheet("border-radius:6px;\n"
"border:1px solid rgb(170, 170, 127);")
        self.old_password_lineedit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.old_password_lineedit.setObjectName("old_password_lineedit")
        self.new_password_linedit = QtWidgets.QLineEdit(self.groupBox)
        self.new_password_linedit.setGeometry(QtCore.QRect(75, 90, 256, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.new_password_linedit.setFont(font)
        self.new_password_linedit.setStyleSheet("border-radius:6px;\n"
"border:1px solid rgb(170, 170, 127);")
        self.new_password_linedit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_password_linedit.setObjectName("new_password_linedit")
        self.reconfirm_password_lineedit = QtWidgets.QLineEdit(self.groupBox)
        self.reconfirm_password_lineedit.setGeometry(QtCore.QRect(75, 135, 256, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reconfirm_password_lineedit.setFont(font)
        self.reconfirm_password_lineedit.setStyleSheet("border-radius:6px;\n"
"border:1px solid rgb(170, 170, 127);")
        self.reconfirm_password_lineedit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.reconfirm_password_lineedit.setObjectName("reconfirm_password_lineedit")
        self.change_password_button = QtWidgets.QPushButton(self.groupBox)
        self.change_password_button.setGeometry(QtCore.QRect(300, 195, 151, 31))
        self.change_password_button.setObjectName("change_password_button")
        self.stackedWidget.addWidget(self.change_password)
        self.remove_ward_page = QtWidgets.QWidget()
        self.remove_ward_page.setObjectName("remove_ward_page")
        self.groupBox_2 = QtWidgets.QGroupBox(self.remove_ward_page)
        self.groupBox_2.setGeometry(QtCore.QRect(180, 90, 481, 211))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(15, 30, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.deletion_password_lineedit = QtWidgets.QLineEdit(self.groupBox_2)
        self.deletion_password_lineedit.setGeometry(QtCore.QRect(30, 90, 256, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.deletion_password_lineedit.setFont(font)
        self.deletion_password_lineedit.setStyleSheet("border: 1px solid rgb(170, 170, 127);\n"
"border-radius:6px;\n"
"")
        self.deletion_password_lineedit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.deletion_password_lineedit.setObjectName("deletion_password_lineedit")
        self.delete_account_button = QtWidgets.QPushButton(self.groupBox_2)
        self.delete_account_button.setGeometry(QtCore.QRect(240, 150, 136, 31))
        self.delete_account_button.setObjectName("delete_account_button")
        self.stackedWidget.addWidget(self.remove_ward_page)
        self.update_ward_profile_page = QtWidgets.QWidget()
        self.update_ward_profile_page.setObjectName("update_ward_profile_page")
        self.groupBox_3 = QtWidgets.QGroupBox(self.update_ward_profile_page)
        self.groupBox_3.setGeometry(QtCore.QRect(105, 45, 721, 421))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("QLineEdit\n"
"{\n"
"    border: 1px solid rgb(170, 170, 127);\n"
"    border-radius:6px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"color:rgb(0, 0, 127);\n"
"}")
        self.groupBox_3.setObjectName("groupBox_3")
        self.municipality_update_lineedit = QtWidgets.QLineEdit(self.groupBox_3)
        self.municipality_update_lineedit.setGeometry(QtCore.QRect(105, 75, 286, 31))
        self.municipality_update_lineedit.setStyleSheet("")
        self.municipality_update_lineedit.setObjectName("municipality_update_lineedit")
        self.address_update_lineedit = QtWidgets.QLineEdit(self.groupBox_3)
        self.address_update_lineedit.setGeometry(QtCore.QRect(105, 120, 286, 31))
        self.address_update_lineedit.setStyleSheet("")
        self.address_update_lineedit.setObjectName("address_update_lineedit")
        self.email_update_lineedit = QtWidgets.QLineEdit(self.groupBox_3)
        self.email_update_lineedit.setGeometry(QtCore.QRect(105, 165, 286, 31))
        self.email_update_lineedit.setObjectName("email_update_lineedit")
        self.phone_update_lineedit = QtWidgets.QLineEdit(self.groupBox_3)
        self.phone_update_lineedit.setGeometry(QtCore.QRect(105, 210, 286, 31))
        self.phone_update_lineedit.setObjectName("phone_update_lineedit")
        self.logo_path_update_lineedit = QtWidgets.QLineEdit(self.groupBox_3)
        self.logo_path_update_lineedit.setGeometry(QtCore.QRect(105, 255, 286, 31))
        self.logo_path_update_lineedit.setObjectName("logo_path_update_lineedit")
        self.state_update_lineedit = QtWidgets.QLineEdit(self.groupBox_3)
        self.state_update_lineedit.setGeometry(QtCore.QRect(435, 120, 151, 31))
        self.state_update_lineedit.setObjectName("state_update_lineedit")
        self.ward_no_update_lineedit = QtWidgets.QLineEdit(self.groupBox_3)
        self.ward_no_update_lineedit.setGeometry(QtCore.QRect(435, 75, 151, 31))
        self.ward_no_update_lineedit.setObjectName("ward_no_update_lineedit")
        self.browse = QtWidgets.QPushButton(self.groupBox_3)
        self.browse.setGeometry(QtCore.QRect(420, 255, 41, 31))
        self.browse.setStyleSheet("border: 2px solid black;\n"
"border-radius:0px;\n"
"border-image:url(:/pic/browse.png);\n"
"\n"
"")
        self.browse.setText("")
        self.browse.setObjectName("browse")
        self.update_ward_profile_button = QtWidgets.QPushButton(self.groupBox_3)
        self.update_ward_profile_button.setGeometry(QtCore.QRect(375, 330, 166, 31))
        self.update_ward_profile_button.setObjectName("update_ward_profile_button")
        self.stackedWidget.addWidget(self.update_ward_profile_page)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        WardWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(WardWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(WardWindow)
        WardWindow.setTabOrder(self.scrollArea, self.home_button)
        WardWindow.setTabOrder(self.home_button, self.settings_button)
        WardWindow.setTabOrder(self.settings_button, self.vital_reg_button)
        WardWindow.setTabOrder(self.vital_reg_button, self.sifarish_button)
        WardWindow.setTabOrder(self.sifarish_button, self.citizenship_button)
        WardWindow.setTabOrder(self.citizenship_button, self.relation_verify_button)
        WardWindow.setTabOrder(self.relation_verify_button, self.old_password_lineedit)
        WardWindow.setTabOrder(self.old_password_lineedit, self.new_password_linedit)
        WardWindow.setTabOrder(self.new_password_linedit, self.reconfirm_password_lineedit)
        WardWindow.setTabOrder(self.reconfirm_password_lineedit, self.change_password_button)
        WardWindow.setTabOrder(self.change_password_button, self.deletion_password_lineedit)
        WardWindow.setTabOrder(self.deletion_password_lineedit, self.delete_account_button)
        WardWindow.setTabOrder(self.delete_account_button, self.municipality_update_lineedit)
        WardWindow.setTabOrder(self.municipality_update_lineedit, self.ward_no_update_lineedit)
        WardWindow.setTabOrder(self.ward_no_update_lineedit, self.address_update_lineedit)
        WardWindow.setTabOrder(self.address_update_lineedit, self.state_update_lineedit)
        WardWindow.setTabOrder(self.state_update_lineedit, self.email_update_lineedit)
        WardWindow.setTabOrder(self.email_update_lineedit, self.phone_update_lineedit)
        WardWindow.setTabOrder(self.phone_update_lineedit, self.logo_path_update_lineedit)
        WardWindow.setTabOrder(self.logo_path_update_lineedit, self.browse)
        WardWindow.setTabOrder(self.browse, self.update_ward_profile_button)

    def retranslateUi(self, WardWindow):
        _translate = QtCore.QCoreApplication.translate
        WardWindow.setWindowTitle(_translate("WardWindow", "SmartWard"))
        self.home_button.setText(_translate("WardWindow", "Home"))
        self.settings_button.setText(_translate("WardWindow", "Settings"))
        self.vital_reg_button.setText(_translate("WardWindow", "Vital Registration"))
        self.citizenship_button.setText(_translate("WardWindow", "Citizenship"))
        self.sifarish_button.setText(_translate("WardWindow", "Sifaris (Recommendation Forms)"))
        self.relation_verify_button.setText(_translate("WardWindow", "Relationship Verification"))
        self.statistics_button.setText(_translate("WardWindow", "Statistics"))
        self.groupBox.setTitle(_translate("WardWindow", "Change Password:"))
        self.old_password_lineedit.setPlaceholderText(_translate("WardWindow", " Current Password"))
        self.new_password_linedit.setPlaceholderText(_translate("WardWindow", " New Password"))
        self.reconfirm_password_lineedit.setPlaceholderText(_translate("WardWindow", " Reconfirm New Password"))
        self.change_password_button.setText(_translate("WardWindow", "Change Password"))
        self.groupBox_2.setTitle(_translate("WardWindow", "Delete Account"))
        self.label.setText(_translate("WardWindow", " Enter password for deletion if you are to delete your account:"))
        self.deletion_password_lineedit.setPlaceholderText(_translate("WardWindow", " Enter password"))
        self.delete_account_button.setText(_translate("WardWindow", "Remove Account"))
        self.groupBox_3.setTitle(_translate("WardWindow", "Ward Profile"))
        self.municipality_update_lineedit.setPlaceholderText(_translate("WardWindow", " Municipality"))
        self.address_update_lineedit.setPlaceholderText(_translate("WardWindow", " Address"))
        self.email_update_lineedit.setPlaceholderText(_translate("WardWindow", " Email address"))
        self.phone_update_lineedit.setPlaceholderText(_translate("WardWindow", " Phone"))
        self.logo_path_update_lineedit.setPlaceholderText(_translate("WardWindow", " Logo path"))
        self.state_update_lineedit.setPlaceholderText(_translate("WardWindow", " State"))
        self.ward_no_update_lineedit.setPlaceholderText(_translate("WardWindow", " Ward No."))
        self.update_ward_profile_button.setText(_translate("WardWindow", "Update Ward Profile"))
import sw_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WardWindow = QtWidgets.QMainWindow()
    ui = Ui_WardWindow()
    ui.setupUi(WardWindow)
    WardWindow.show()
    sys.exit(app.exec_())
