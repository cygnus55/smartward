from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import pickle
import nepali_date
import sw_string
import num2words
from sw_pdf import Receipt


class Ui_Receiptwindow(QWidget):
    def setupUi(self, Receiptwindow):
        Receiptwindow.setObjectName("Receiptwindow")
        Receiptwindow.resize(488, 429)
        self.centralwidget = QtWidgets.QWidget(Receiptwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 468, 409))
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
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        self.tableWidget.setColumnWidth(0,15)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        self.tableWidget.setColumnWidth(1, 300)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setColumnWidth(2,88)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.tableWidget)
        self.totalLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.totalLabel.setObjectName("totalLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.totalLabel)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.scrollAreaWidgetContents)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.gridLayout_2.addLayout(self.formLayout_2, 3, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        Receiptwindow.setCentralWidget(self.centralwidget)

        Receiptwindow.setMinimumSize(500,430)
        Receiptwindow.setMaximumSize(500,430)
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
        self.totalLabel.setText(_translate("Receiptwindow", "<b>Total:"))
        self.label.setText(_translate("Receiptwindow", "<b>Amount In word:"))
        self.pushButton.setText(_translate("Receiptwindow", "Add"))


class ActualWork():
    def __init__(self):
        import dbconnect
        self.db = dbconnect.database_receipt("localhost", "root")
        self.db.createReceiptGenerateTable()
        self.receiptForm = QtWidgets.QMainWindow()
        self.ui = Ui_Receiptwindow()
        self.ui.setupUi(self.receiptForm)
        self.receiptForm.show()
        self.actualWork()

    def addMore(self):
        if(self.addToReceiptGenerate()):
            i = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(i)
        self.showTotal()

    def addToReceiptGenerate(self):
        row = self.ui.tableWidget.rowCount()
        cols = self.ui.tableWidget.columnCount()
        rowdata=[]
        for c in range(0,cols):
            data=self.ui.tableWidget.item(row-1,c).text()
            try:
                if c==0 or c==2 :
                    data=int(data)
                rowdata.append(data)
            except Exception as e:
                    QMessageBox.warning(self.ui,"Receipt","Invalid Amount")
                    rowdata.pop(row-1)
                    return False
        self.db.insertintoreceiptgenerate(rowdata)
        return True

    def showTotal(self):
        total=self.db.selectAmountfromReceiptGenerate()
        self.ui.label_2.setText("Rs. "+str(total)+"/-")
        self.ui.label_3.setText("Rs. "+num2words.num2words(total).title()+" Only.")

    def actualWork(self):
        self.ui.pushButton.clicked.connect(self.addMore)
        self.ui.buttonBox.accepted.connect(self.operateReceipt)
        self.ui.buttonBox.rejected.connect(lambda: self.receiptForm.close())

    def printReceipt(self):
        rows = self.ui.tableWidget.rowCount()
        cols = self.ui.tableWidget.columnCount()
        detailsofreceipt= [['S.N.','Details','Amount']]
        for r in range(0, rows):
            row = []
            for c in range(0, cols):
                try:
                    i = self.ui.tableWidget.item(r, c)
                    row.append(i.text())
                except AttributeError:
                    i = '-'
                    row.append(i)
            detailsofreceipt.append(row)
        tabledata = detailsofreceipt
        receiptno = self.ui.receiptNoLineEdit.text()
        name = self.ui.nameLineEdit.text()
        total = (str(self.ui.label_2.text()),self.ui.label_3.text())
        body=(receiptno,name,total)
        receipt=(body,tabledata)
        #print receipt
        rcp=Receipt()
        rcp.setBody(receipt)
        rcp.output()
        QMessageBox.information(self.ui,"Receipt","Sucessful")

    def operateReceipt(self):
        self.printReceipt()
        self.db.dropReceiptGenerate()
        self.db.createReceiptTable()
        today = nepali_date.NepaliDate.today()
        today_date = str(today)[3:]
        receiptno=self.ui.receiptNoLineEdit.text()
        name=self.ui.nameLineEdit.text()
        total=str(self.ui.label_2.text())
        totalamount=int(total[4:len(total)-2])
        rowdata=(today_date,receiptno,name,totalamount)
        self.db.insertintoreceipt(rowdata)

    def closeActualWork(self):
        self.receiptForm.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    aw = ActualWork()
    '''
    Receiptwindow = QtWidgets.QMainWindow()
    ui = Ui_Receiptwindow()
    ui.setupUi(Receiptwindow)
    Receiptwindow.show()
    '''
    sys.exit(app.exec_())
