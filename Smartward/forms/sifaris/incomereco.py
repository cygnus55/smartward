from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import num2words
import datetime
import nepali_date
import sw_string
import pickle
from sw_pdf import IncomeReco

class Ui_incomereco(QWidget):
    def setupUi(self, incomereco):
        incomereco.setObjectName("incomereco")
        incomereco.resize(888, 989)
        incomereco.setMinimumSize(QtCore.QSize(550, 500))
        incomereco.setMaximumSize(QtCore.QSize(550, 500))
        self.centralwidget = QtWidgets.QWidget(incomereco)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.fatherNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.fatherNameLabel.setObjectName("fatherNameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.fatherNameLabel)
        self.fatherNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.fatherNameLineEdit.setObjectName("fatherNameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fatherNameLineEdit)
        self.AddressLabel = QtWidgets.QLabel(self.centralwidget)
        self.AddressLabel.setObjectName("AddressLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.AddressLabel)
        self.wardNoLabel = QtWidgets.QLabel(self.centralwidget)
        self.wardNoLabel.setObjectName("wardNoLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.wardNoLabel)
        self.wardNoLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.wardNoLineEdit.setObjectName("wardNoLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.wardNoLineEdit)
        self.municipalityLabel = QtWidgets.QLabel(self.centralwidget)
        self.municipalityLabel.setObjectName("municipalityLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.municipalityLabel)
        self.municipalityLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.municipalityLineEdit.setObjectName("municipalityLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.municipalityLineEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.formLayout.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.setColumnWidth(0, 25)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.setColumnWidth(1, 220)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.setColumnWidth(2, 100)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.setColumnWidth(3, 200)
        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 1)
        incomereco.setCentralWidget(self.centralwidget)

        self.pushButton.clicked.connect(self.addMoreDetail)
        self.retranslateUi(incomereco)
        QtCore.QMetaObject.connectSlotsByName(incomereco)

    def addMoreDetail(self):
        i=self.tableWidget.rowCount()
        self.tableWidget.insertRow(i)

    def retranslateUi(self, incomereco):
        _translate = QtCore.QCoreApplication.translate
        incomereco.setWindowTitle(_translate("incomereco", "Income Source Recommendation"))
        self.nameLabel.setText(_translate("incomereco", "Name"))
        self.fatherNameLabel.setText(_translate("incomereco", "Father\'s Name"))
        self.AddressLabel.setText(_translate("incomereco", "<b>Address"))
        self.wardNoLabel.setText(_translate("incomereco", "Ward No."))
        self.municipalityLabel.setText(_translate("incomereco", "Municipality"))
        self.pushButton.setText(_translate("incomereco", "Add"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("incomereco", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("incomereco", "S.N."))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("incomereco", "Details"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("incomereco", "Amount"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("incomereco", "Remarks"))
        self.nameLabel.setText(_translate("incomereco", "Name"))

class ActualWork():
    def __init__(self):
        self.incomerecoForm = QtWidgets.QMainWindow()
        self.ui = Ui_incomereco()
        self.ui.setupUi(self.incomerecoForm)
        self.incomerecoForm.show()
        self.actualWork()

    def actualWork(self):
        self.ui.buttonBox.accepted.connect(self.submitform)
        self.ui.buttonBox.rejected.connect(lambda: self.incomerecoForm.close())

    def submitform(self):
        self.getallvalues()
        self.getRecommendation()

    def getallvalues(self):
        address=(
            self.ui.wardNoLineEdit.text(),self.ui.municipalityLineEdit.text()
        )
        detailsofincome = [['SN', 'Details', 'Amount', 'Remarks']]
        income = []
        rows = self.ui.tableWidget.rowCount()
        cols = self.ui.tableWidget.columnCount()
        for r in range(0, rows):
            row = []
            income.append(int(self.ui.tableWidget.item(r,2).text()))
            for c in range(0, cols):
                try:
                    i = self.ui.tableWidget.item(r, c)
                    row.append(i.text())
                except AttributeError:
                    i = '-'
                    row.append(i)
            detailsofincome.append(row)
        tabledata=detailsofincome
        total=0
        for amount in income:
            total+=amount
        totalincome=(total,num2words.num2words(total))
        body=(self.ui.nameLineEdit.text(),self.ui.fatherNameLineEdit.text(),address[0],address[1])
        rec=(body,tabledata,totalincome)
        self.writePickle(rec)


    def writePickle(self, d):
        with open("recommendation.pickle", "wb") as obj:
            pickle.dump(d, obj)
            obj.close()

    def getRecommendation(self):
        QMessageBox.information(self.ui, "Income Recommendation","Get Income Recommendation Letter.")
        recommendation = IncomeReco()
        f = open("recommendation.pickle", 'rb')
        rec = pickle.load(f)
        print(rec[0])
        recommendation.setBody(rec[0])
        recommendation.setTable(rec[1])
        recommendation.setTotalIncome(rec[2])
        recommendation.output()
        QMessageBox.information(self.ui, "Income Recommendation", "Income Recommendation was Sucessful.")

    def closeActualWork(self):
        self.incomerecoForm.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    aw = ActualWork()
    '''
    incomereco = QtWidgets.QMainWindow()
    ui = Ui_incomereco()
    ui.setupUi(incomereco)
    incomereco.show()
    '''
    sys.exit(app.exec_())
