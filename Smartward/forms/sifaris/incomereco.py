# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'incomesourcerecommendation.ui'
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
table="incomerecoregistration"


class Ui_incomereco(object):
    def setupUi(self, incomereco):
        incomereco.setObjectName("incomereco")
        incomereco.resize(529, 600)
        self.centralwidget = QtWidgets.QWidget(incomereco)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.registrationNoLabel = QtWidgets.QLabel(self.centralwidget)
        self.registrationNoLabel.setObjectName("registrationNoLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.registrationNoLabel)
        self.registrationNoLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.registrationNoLineEdit.setObjectName("registrationNoLineEdit")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.registrationNoLineEdit)
        self.gridLayout.addLayout(self.formLayout_3, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
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
        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.majorIncomeSourceLabel = QtWidgets.QLabel(self.centralwidget)
        self.majorIncomeSourceLabel.setObjectName("majorIncomeSourceLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.majorIncomeSourceLabel)
        self.majorIncomeSourceLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.majorIncomeSourceLineEdit.setObjectName("majorIncomeSourceLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.majorIncomeSourceLineEdit)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)
        incomereco.setCentralWidget(self.centralwidget)

        self.retranslateUi(incomereco)
        QtCore.QMetaObject.connectSlotsByName(incomereco)

    def retranslateUi(self, incomereco):
        _translate = QtCore.QCoreApplication.translate
        incomereco.setWindowTitle(_translate("incomereco", "Income Source Recommendation"))
        self.registrationNoLabel.setText(_translate("incomereco", "Registration No"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("incomereco", "S.N."))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("incomereco", "Details"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("incomereco", "Amount"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("incomereco", "Time"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("incomereco", "Remarks"))
        self.nameLabel.setText(_translate("incomereco", "Name"))
        self.majorIncomeSourceLabel.setText(_translate("incomereco", "Major Income Source"))
class ActualWork():
    def __init__(self):
        import dbconnect
        self.db = dbconnect.database_wardwindow("localhost", "root")
        self.incomerecoForm = QtWidgets.QMainWindow()
        self.ui = Ui_incomereco()
        self.ui.setupUi(self.incomerecoForm)
        self.incomerecoForm.show()
        self.actualWork()
    def actualWork(self):
        self.ui.buttonBox.accepted.connect(self.submitform)
        self.ui.buttonBox.rejected.connect(lambda: self.incomerecoForm.close())

    def submitform(self):
        self.values = self.getallvalues()
        a = sw_string.generateList(**self.values)
        self.db.createFormTable(table)
        self.db.addColumns(table, a[4], a[6])
        self.db.insertValues(table, a)
    def getallvalues(self):
        self.incomeRegNo=self.ui.registrationNoLineEdit.text()
        today = nepali_date.NepaliDate.today()
        registrationdate = str(today)[3:]
        detailsofparent=(self.ui.nameLineEdit.text(),self.ui.majorIncomeSourceLineEdit.text())
        detailsofincome=[['SN','Details','Amount','Time']]
        for r in range(0,5):
            row=[]
            for c in range(0,4):
                try:
                    i=self.ui.tableWidget.item(r,c)
                    row.append(i.text())
                except AttributeError:
                    i='-'
                    row.append(i)
            detailsofincome.append(row)
        return {"RegDate": registrationdate, "RegNo": self.incomeRegNo,"parentdetail":str(detailsofparent),"incomedetails":str(detailsofincome)}
                    
    def closeActualWork(self):
        self.incomerecoForm.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aw=ActualWork()
    '''
    incomereco = QtWidgets.QMainWindow()
    ui = Ui_incomereco()
    ui.setupUi(incomereco)
    incomereco.show()
    '''
    sys.exit(app.exec_())
