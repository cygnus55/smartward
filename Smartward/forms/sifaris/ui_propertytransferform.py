# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'properttransferform.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 560))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.propertyHolderDetailSLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.propertyHolderDetailSLabel.setObjectName("propertyHolderDetailSLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.propertyHolderDetailSLabel)
        self.fullNameLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.fullNameLabel.setObjectName("fullNameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.fullNameLabel)
        self.fullNameLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.fullNameLineEdit.setObjectName("fullNameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fullNameLineEdit)
        self.dateOfDeathLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.dateOfDeathLabel.setObjectName("dateOfDeathLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.dateOfDeathLabel)
        self.dateOfDeathDateEdit = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        self.dateOfDeathDateEdit.setObjectName("dateOfDeathDateEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dateOfDeathDateEdit)
        self.kitaNoLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.kitaNoLabel.setObjectName("kitaNoLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.kitaNoLabel)
        self.kitaNoLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.kitaNoLineEdit.setObjectName("kitaNoLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.kitaNoLineEdit)
        self.TransferedDetailsLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.TransferedDetailsLabel.setObjectName("TransferedDetailsLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.TransferedDetailsLabel)
        self.nameLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.relationWithDeceisedLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.relationWithDeceisedLabel.setObjectName("relationWithDeceisedLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.relationWithDeceisedLabel)
        self.relationWithDeceisedComboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.relationWithDeceisedComboBox.setObjectName("relationWithDeceisedComboBox")
        self.relationWithDeceisedComboBox.addItem("")
        self.relationWithDeceisedComboBox.addItem("")
        self.relationWithDeceisedComboBox.addItem("")
        self.relationWithDeceisedComboBox.addItem("")
        self.relationWithDeceisedComboBox.addItem("")
        self.relationWithDeceisedComboBox.addItem("")
        self.relationWithDeceisedComboBox.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.relationWithDeceisedComboBox)
        self.pushButton_submit = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_submit.setObjectName("pushButton_submit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.pushButton_submit)
        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Property  Transfer"))
        self.propertyHolderDetailSLabel.setText(_translate("MainWindow", "Property holder detail\'s"))
        self.fullNameLabel.setText(_translate("MainWindow", "Full Name"))
        self.dateOfDeathLabel.setText(_translate("MainWindow", "Date of death"))
        self.kitaNoLabel.setText(_translate("MainWindow", "Kita No"))
        self.TransferedDetailsLabel.setText(_translate("MainWindow", "Property to be transfered details"))
        self.nameLabel.setText(_translate("MainWindow", "Full Name"))
        self.relationWithDeceisedLabel.setText(_translate("MainWindow", "Relation with deceised"))
        self.relationWithDeceisedComboBox.setItemText(0, _translate("MainWindow", "Husband"))
        self.relationWithDeceisedComboBox.setItemText(1, _translate("MainWindow", "Wife"))
        self.relationWithDeceisedComboBox.setItemText(2, _translate("MainWindow", "Son"))
        self.relationWithDeceisedComboBox.setItemText(3, _translate("MainWindow", "Daughter"))
        self.relationWithDeceisedComboBox.setItemText(4, _translate("MainWindow", "Father"))
        self.relationWithDeceisedComboBox.setItemText(5, _translate("MainWindow", "Mother"))
        self.relationWithDeceisedComboBox.setItemText(6, _translate("MainWindow", "other"))
        self.pushButton_submit.setText(_translate("MainWindow", "Submit"))


