# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gharbato.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(639, 482)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 619, 462))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.gridLayout_2.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.permanentAddressLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.permanentAddressLabel.setObjectName("permanentAddressLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.permanentAddressLabel)
        self.permanentAddressLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.permanentAddressLineEdit.setObjectName("permanentAddressLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.permanentAddressLineEdit)
        self.addressOfMalpotLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.addressOfMalpotLabel.setObjectName("addressOfMalpotLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.addressOfMalpotLabel)
        self.addressOfMalpotLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.addressOfMalpotLineEdit.setObjectName("addressOfMalpotLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.addressOfMalpotLineEdit)
        self.citizenshipNoLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.citizenshipNoLabel.setObjectName("citizenshipNoLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.citizenshipNoLabel)
        self.citizenshipNoLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.citizenshipNoLineEdit.setObjectName("citizenshipNoLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.citizenshipNoLineEdit)
        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)
        self.pushButton_submit = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_submit.setObjectName("pushButton_submit")
        self.gridLayout_2.addWidget(self.pushButton_submit, 2, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "Municipality/Rural Municipality"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "Ward No."))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("mainWindow", "Kitta No."))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("mainWindow", "Area"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("mainWindow", "House Details"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("mainWindow", "Description of the route"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("mainWindow", "Remarks"))
        self.nameLabel.setText(_translate("mainWindow", "Name"))
        self.permanentAddressLabel.setText(_translate("mainWindow", "PermanentAddress"))
        self.addressOfMalpotLabel.setText(_translate("mainWindow", "Address of Malpot Office"))
        self.citizenshipNoLabel.setText(_translate("mainWindow", "Citizenship No."))
        self.pushButton_submit.setText(_translate("mainWindow", "Submit"))


