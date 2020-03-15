# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gharbato.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

import nepali_date
import num2words
import pickle
from sw_pdf import GharBatoReco



class Ui_mainWindow(QWidget):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(713, 583)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 693, 563))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.setColumnWidth(0,125)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.setColumnWidth(1, 100)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.setColumnWidth(2, 150)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.setColumnWidth(3, 150)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.setColumnWidth(4, 200)
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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.scrollAreaWidgetContents)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.pushButton.clicked.connect(self.addMoreDetail)
        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def addMoreDetail(self):
        i=self.tableWidget.rowCount()
        self.tableWidget.insertRow(i)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "Kitta No."))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "Area"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("mainWindow", "House Details"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("mainWindow", "Route Description"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("mainWindow", "Remarks"))
        self.nameLabel.setText(_translate("mainWindow", "Name <font color=\'red\'>*"))
        self.permanentAddressLabel.setText(_translate("mainWindow", "PermanentAddress <font color=\'red\'>*"))
        self.permanentAddressLineEdit.setPlaceholderText(_translate("mainWindow", "Ward No., Municipality, District"))
        self.addressOfMalpotLabel.setText(_translate("mainWindow", "Address of Malpot Office <font color=\'red\'>*"))
        self.citizenshipNoLabel.setText(_translate("mainWindow", "Citizenship No. <font color=\'red\'>*"))
        self.pushButton.setText(_translate("mainWindow", "Add"))

class ActualWork():
    def __init__(self):
        self.gharbatoForm = QtWidgets.QMainWindow()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self.gharbatoForm)
        self.gharbatoForm.show()
        self.actualWork()
    
    def actualWork(self):
        self.ui.buttonBox.accepted.connect(self.submitform)
        self.ui.buttonBox.rejected.connect(lambda: self.gharbatoForm.close())

    def submitform(self):
        if (self.checkEmpty()):
            QMessageBox.warning(self.ui,"Road Network Verification Recommendation","All * field should be filled.")
        else:
            self.getallvalues()
            self.getRecommendation()
            #QMessageBox.warning(self.ui,"Road Network Verification Recommendation","All * field should be filled.")

    def checkEmpty(self):
        A=self.ui.nameLineEdit.text().strip()
        B=self.ui.permanentAddressLineEdit.text().strip()
        C=self.ui.addressOfMalpotLineEdit.text().strip()
        D=self.ui.citizenshipNoLineEdit.text().strip()
        if(A=='' or B==''  or C==''  or D=='' ):
            return True
        return False

    def getallvalues(self):
        body=(self.ui.nameLineEdit.text(),self.ui.permanentAddressLineEdit.text(),self.ui.addressOfMalpotLineEdit.text(),self.ui.citizenshipNoLineEdit.text())
        detailsofproperty=[['Kitta No.','Area','House Details','Route Description','Remarks']]
        rows = self.ui.tableWidget.rowCount()
        cols = self.ui.tableWidget.columnCount()
        for r in range(0, rows):
            row = []
            for c in range(0, cols):
                try:
                    i = self.ui.tableWidget.item(r, c)
                    row.append(i.text())
                except AttributeError:
                    i = '-'
                    row.append(i)
            detailsofproperty.append(row)
        tabledata=detailsofproperty
        rec=(body,tabledata)
        self.writePickle(rec)
    
    def writePickle(self, d):
        with open("recommendation.pickle", "wb") as obj:
            pickle.dump(d, obj)
            obj.close()

    def getRecommendation(self):
        QMessageBox.information(self.ui, "Road Network Verification Recommendation","Get Road Network Verification Recommendation Letter.")
        recommendation = GharBatoReco()
        f = open("recommendation.pickle", 'rb')
        rec = pickle.load(f)
        #print(rec[0])
        recommendation.setBody(rec[0])
        recommendation.setTable(rec[1])
        recommendation.setRegistrar()
        recommendation.output()
        QMessageBox.information(self.ui, "Road Network Verification Recommendation", "Road Network Verification Recommendation was Sucessful.")

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
