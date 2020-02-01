# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Homepage.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_homeWindow(object):
    def setupUi(self, homeWindow):
        homeWindow.setObjectName("homeWindow")
        homeWindow.resize(1920, 1080)
        homeWindow.setMinimumSize(QtCore.QSize(1920, 1080))
        homeWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget = QtWidgets.QWidget(homeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_logo = QtWidgets.QFrame(self.centralwidget)
        self.frame_logo.setGeometry(QtCore.QRect(0, 0, 1920, 200))
        self.frame_logo.setStyleSheet("background-color: rgb(170, 0, 127);")
        self.frame_logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_logo.setObjectName("frame_logo")
        self.label_logo = QtWidgets.QLabel(self.frame_logo)
        self.label_logo.setGeometry(QtCore.QRect(50, 40, 171, 111))
        self.label_logo.setObjectName("label_logo")
        self.label_info = QtWidgets.QLabel(self.frame_logo)
        self.label_info.setGeometry(QtCore.QRect(260, 40, 941, 111))
        self.label_info.setObjectName("label_info")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 200, 1920, 50))
        self.frame.setStyleSheet("background-color: rgb(130, 255, 193);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_home = QtWidgets.QPushButton(self.frame)
        self.pushButton_home.setGeometry(QtCore.QRect(20, 10, 111, 41))
        self.pushButton_home.setObjectName("pushButton_home")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 250, 1920, 930))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pushButton_death = QtWidgets.QPushButton(self.page)
        self.pushButton_death.setGeometry(QtCore.QRect(400, 280, 480, 100))
        self.pushButton_death.setObjectName("pushButton_death")
        self.pushButton_divorce = QtWidgets.QPushButton(self.page)
        self.pushButton_divorce.setGeometry(QtCore.QRect(1100, 90, 480, 100))
        self.pushButton_divorce.setObjectName("pushButton_divorce")
        self.pushButton_marriage = QtWidgets.QPushButton(self.page)
        self.pushButton_marriage.setGeometry(QtCore.QRect(1100, 280, 480, 100))
        self.pushButton_marriage.setObjectName("pushButton_marriage")
        self.pushButton_birth = QtWidgets.QPushButton(self.page)
        self.pushButton_birth.setGeometry(QtCore.QRect(400, 90, 480, 100))
        self.pushButton_birth.setObjectName("pushButton_birth")
        self.pushButton_migration = QtWidgets.QPushButton(self.page)
        self.pushButton_migration.setGeometry(QtCore.QRect(400, 470, 480, 100))
        self.pushButton_migration.setObjectName("pushButton_migration")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        homeWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(homeWindow)
        self.statusbar.setObjectName("statusbar")
        homeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(homeWindow)
        QtCore.QMetaObject.connectSlotsByName(homeWindow)

    def retranslateUi(self, homeWindow):
        _translate = QtCore.QCoreApplication.translate
        homeWindow.setWindowTitle(_translate("homeWindow", "MainWindow"))
        self.label_logo.setText(_translate("homeWindow", "LOGO"))
        self.label_info.setText(_translate("homeWindow", "INFO"))
        self.pushButton_home.setToolTip(_translate("homeWindow", "haha"))
        self.pushButton_home.setText(_translate("homeWindow", "Home"))
        self.pushButton_death.setText(_translate("homeWindow", "Death"))
        self.pushButton_divorce.setText(_translate("homeWindow", "Divorce"))
        self.pushButton_marriage.setText(_translate("homeWindow", "Marriage"))
        self.pushButton_birth.setText(_translate("homeWindow", "Birth"))
        self.pushButton_migration.setText(_translate("homeWindow", "Migration"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    homeWindow = QtWidgets.QMainWindow()
    ui = Ui_homeWindow()
    ui.setupUi(homeWindow)
    homeWindow.show()
    sys.exit(app.exec_())
