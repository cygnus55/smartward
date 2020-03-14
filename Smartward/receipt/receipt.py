# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'receipt.ui'
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
import inflect
table="ReceiptRegistration"



class Ui_Receiptwindow(object):
    def setupUi(self, Receiptwindow):
        Receiptwindow.setObjectName("Receiptwindow")
        Receiptwindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Receiptwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 776, 576))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.receiptNoLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.receiptNoLabel.setObjectName("receiptNoLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.receiptNoLabel)
        self.receiptNoLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.receiptNoLineEdit.setObjectName("receiptNoLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.receiptNoLineEdit)
        self.nameLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.tableWidget)
        self.totalLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.totalLabel.setObjectName("totalLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.totalLabel)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.label_2)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.label_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.scrollAreaWidgetContents)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.buttonBox)
        self.gridLayout_2.addLayout(self.formLayout_2, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        Receiptwindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(Receiptwindow)
        QtCore.QMetaObject.connectSlotsByName(Receiptwindow)

    def retranslateUi(self, Receiptwindow):
        _translate = QtCore.QCoreApplication.translate
        Receiptwindow.setWindowTitle(_translate("Receiptwindow", "Receipt"))
        self.receiptNoLabel.setText(_translate("Receiptwindow", "Receipt No"))
        self.nameLabel.setText(_translate("Receiptwindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Receiptwindow", "S.N"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Receiptwindow", "Description"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Receiptwindow", "Amount"))
        self.totalLabel.setText(_translate("Receiptwindow", "Total"))
        self.label_2.setText(_translate("Receiptwindow", ""))
        self.label.setText(_translate("Receiptwindow", "Amount In word"))
        self.label_3.setText(_translate("Receiptwindow", " "))
class ActualWork():
    def __init__(self):
        import dbconnect
        self.db = dbconnect.database_wardwindow("localhost", "root")
        self.receiptForm = QtWidgets.QMainWindow()
        self.ui = Ui_Receiptwindow()
        self.ui.setupUi(self.receiptForm)
        self.receiptForm.show()
        self.actualWork()
    def actualWork(self):
        self.ui.buttonBox.accepted.connect(self.submitform)
        self.ui.buttonBox.rejected.connect(lambda: self.receiptForm.close())

    def submitform(self):
        self.values = self.getallvalues()
        a = sw_string.generateList(**self.values)
        self.db.createFormTable(table)
        self.db.addColumns(table, a[4], a[6],a[8],a[10])
        self.db.insertValues(table, a)
    def getallvalues(self):
        self.receiptNo=self.ui.receiptNoLineEdit.text()
        self.name=self.ui.nameLineEdit.text()
        today = nepali_date.NepaliDate.today()
        registrationdate = str(today)[3:]
        detailsofreceipt=[['SN','Description','Amount']]
        a=0
        for r in range(0,3):
            row=[]
            for c in range(0,3):
                try:
                    i=self.ui.tableWidget.item(r,c)
                    b=self.ui.tableWidget.item(r,2).text()
                    a=int(b)+a
                    row.append(i.text())
                except AttributeError:
                    i='-'
                    row.append(i)
            detailsofreceipt.append(row)
        print (a)
        self.total=self.ui.label_2.setText(str(a))
        p= inflect. engine()
        amount= p. number_to_words(self.total)
        self.amountinword=self.ui.label_3.setText(amount)
        return {"RegDate": registrationdate, "receiptno":self.receiptNo,"name":self.name,"receiptdetail":str(detailsofreceipt),"total":str(self.total),"amount inword":str(self.amountinword)}
                    

        
        
        
            
        
    def closeActualWork(self):
        self.receiptForm.close()

        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aw=ActualWork()
    '''
    Receiptwindow = QtWidgets.QMainWindow()
    ui = Ui_Receiptwindow()
    ui.setupUi(Receiptwindow)
    Receiptwindow.show()
    '''
    sys.exit(app.exec_())
