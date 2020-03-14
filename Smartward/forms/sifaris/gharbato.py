# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gharbato.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import datetime
import nepali_date
import sw_string
table="Gharbatoregistration"


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(888, 989)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 615, 458))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.registrationNoLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.registrationNoLabel.setObjectName("registrationNoLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.registrationNoLabel)
        self.registrationNoLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.registrationNoLineEdit.setObjectName("registrationNoLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.registrationNoLineEdit)
        self.gridLayout_2.addLayout(self.formLayout_2, 0, 0, 1, 1)
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
        self.gridLayout_2.addWidget(self.tableWidget, 2, 0, 1, 1)
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
        self.gridLayout_2.addLayout(self.formLayout, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.scrollAreaWidgetContents)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 3, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.registrationNoLabel.setText(_translate("mainWindow", "Registration no"))
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
class ActualWork():
    def __init__(self):
        import dbconnect
        self.db = dbconnect.database_wardwindow("localhost", "root")
        self.gharbatoForm = QtWidgets.QMainWindow()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self.gharbatoForm)
        self.gharbatoForm.show()
        self.actualWork()
    
    def actualWork(self):
        self.ui.buttonBox.accepted.connect(self.submitform)
        self.ui.buttonBox.rejected.connect(lambda: self.gharbatoForm.close())
    def submitform(self):
        self.values = self.getallvalues()
        a = sw_string.generateList(**self.values)
        self.db.createFormTable(table)
        self.db.addColumns(table, a[4], a[6])
        self.db.insertValues(table, a)
    def getallvalues(self):
        self.batoregNo=self.ui.registrationNoLineEdit.text()
        today = nepali_date.NepaliDate.today()
        registrationdate = str(today)[3:]
        detailsofperson=(self.ui.nameLineEdit.text(),self.ui.permanentAddressLineEdit.text(),self.ui.addressOfMalpotLineEdit.text(),self.ui.citizenshipNoLineEdit.text())
        detailsofproperty=[]
        for r in range(0,1):
            for c in range(0,7):
                try:
                    i=self.ui.tableWidget.item(r,c)
                    detailsofproperty.append(i.text())
                except:
                    i='-'
                    detailsofproperty.append(i)
        return {"RegDate": registrationdate, "RegNo": self.batoregNo,"detailsofperson":str(detailsofperson),"detailsofproperty":str(detailsofproperty)}
    
        
                
        
    def closeActualWork(self):
        self.gharbatoForm.close()
        


        




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aw=ActualWork()
    '''
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    '''
    sys.exit(app.exec_())
