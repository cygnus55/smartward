# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'propertytransferform.ui'
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
table="propertytransferRegistration"



class Ui_propertytransfer(object):
    def setupUi(self, propertytransfer):
        propertytransfer.setObjectName("propertytransfer")
        propertytransfer.resize(800, 628)
        self.centralwidget = QtWidgets.QWidget(propertytransfer)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 776, 579))
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
        self.buttonBox = QtWidgets.QDialogButtonBox(self.scrollAreaWidgetContents)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        self.gridLayout_2.addLayout(self.formLayout, 1, 0, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.registrationNoLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.registrationNoLabel.setObjectName("registrationNoLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.registrationNoLabel)
        self.registrationNoLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.registrationNoLineEdit.setObjectName("registrationNoLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.registrationNoLineEdit)
        self.gridLayout_2.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        propertytransfer.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(propertytransfer)
        self.statusbar.setObjectName("statusbar")
        propertytransfer.setStatusBar(self.statusbar)

        self.retranslateUi(propertytransfer)
        QtCore.QMetaObject.connectSlotsByName(propertytransfer)

    def retranslateUi(self, propertytransfer):
        _translate = QtCore.QCoreApplication.translate
        propertytransfer.setWindowTitle(_translate("propertytransfer", "Property  Transfer"))
        self.propertyHolderDetailSLabel.setText(_translate("propertytransfer", "Property holder detail\'s"))
        self.fullNameLabel.setText(_translate("propertytransfer", "Full Name"))
        self.dateOfDeathLabel.setText(_translate("propertytransfer", "Date of death"))
        self.kitaNoLabel.setText(_translate("propertytransfer", "Kita No"))
        self.TransferedDetailsLabel.setText(_translate("propertytransfer", "Property to be transfered details"))
        self.nameLabel.setText(_translate("propertytransfer", "Full Name"))
        self.relationWithDeceisedLabel.setText(_translate("propertytransfer", "Relation with deceised"))
        self.relationWithDeceisedComboBox.setItemText(0, _translate("propertytransfer", "Husband"))
        self.relationWithDeceisedComboBox.setItemText(1, _translate("propertytransfer", "Wife"))
        self.relationWithDeceisedComboBox.setItemText(2, _translate("propertytransfer", "Son"))
        self.relationWithDeceisedComboBox.setItemText(3, _translate("propertytransfer", "Daughter"))
        self.relationWithDeceisedComboBox.setItemText(4, _translate("propertytransfer", "Father"))
        self.relationWithDeceisedComboBox.setItemText(5, _translate("propertytransfer", "Mother"))
        self.relationWithDeceisedComboBox.setItemText(6, _translate("propertytransfer", "other"))
        self.registrationNoLabel.setText(_translate("propertytransfer", "Registration no"))
class ActualWork():
    def __init__(self):
        import dbconnect
        self.db=dbconnect.database_wardwindow("localhost","root")
        self.ptransferForm = QtWidgets.QMainWindow()
        self.ui = Ui_propertytransfer()
        self.ui.setupUi(self.ptransferForm)
        self.ptransferForm.show()
        self.actualWork()

    def actualWork(self):
        self.ui.buttonBox.accepted.connect(self.submitform)
        self.ui.buttonBox.rejected.connect(lambda:self.ptransferForm.close())

    def submitform(self):
        self.values=self.getallvalues()
        a=sw_string.generateList(**self.values)
        #a=["RegDate","1","RegNo","2","C","3","D","4","E","5"]
        #b=['RegNo','123-32','detailsofmarriage', "('Social Tradition', ('2000-01-01', '2056/09/17'))", 'locationofmarriage', "('Kavre', 'Namobudda', '04', 'Timal Road', 'Methinkot', '45', '')", 'detailsofspouse', "{'detailsofbride': ('Tandon', 'Rabina', '2057/01/05', 'Kami', '+2', 'Actress', 'Divorcee', ('Rampur', 'Narayanghat', '5', 'Ghandi Street', 'Hariharpur', '78', 'India'), ('India', '27-12398721', '2071/06/09', 'Rampur', '87289398', 'India', 'New Delhi'), ('Fariha Tandon', 'Kanod Tandon', 'Kajol Tandon')), 'detailsofbridegroom': ('Ghimere', 'Tilak', '2051/03/21', 'Brahmin', 'B.Sc.', 'Astrologer', 'Single', ('Solukhumbu', 'Namche Bazar', '9', 'Manila Street', 'Vaisepati', '567', 'Nepal'), ('Nepal', '983-3468', '2067/03/05', 'Solukhumbu', '', '', ''), ('Goshnath Ghimere', 'Farilal Ghimere', 'Nabina Ghimere'))}"]
        #a=['RegDate',,b[0],b[1],b[2],b[3].replace("'","__"),b[4],b[5].replace("'","__"),b[6],b[7].replace("'","__")]
        #print(a)
        self.db.createFormTable(table)
        self.db.addColumns(table,a[4],a[6])
        self.db.insertValues(table,a)

    def getallvalues(self):
        self.ptransferRegNo=self.ui.registrationNoLineEdit.text()
        date=QDate(self.ui.dateOfDeathDateEdit.date())
        year,month,day=date.getDate()
        death_in_ad=datetime.date(year,month,day)
        death_in_bs=nepali_date.NepaliDate.to_nepali_date(death_in_ad)
        today=nepali_date.NepaliDate.today()
        #registration date
        registrationdate=str(today)[3:]
        #concerned person death date
        self.deathdate=(str(death_in_ad),str(death_in_bs)[3:])
        #propertyholder details
        propertyholder=(self.ui.fullNameLineEdit.text(),self.deathdate,self.ui.kitaNoLineEdit.text())
        #property to be transfered detail
        propertytobetransfered=(self.ui.nameLineEdit.text(),self.ui.relationWithDeceisedComboBox.currentText())
        return {"RegDate":registrationdate,"RegNo":self.ptransferRegNo,"propertyholder":str(propertyholder) , "propertytobetransferd":str(propertytobetransfered)}

        
    def closeActualWork(self):
        self.ptransferForm.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aw=ActualWork()
    '''
    propertytransfer = QtWidgets.QMainWindow()
    ui = Ui_propertytransfer()
    ui.setupUi(propertytransfer)
    propertytransfer.show()
    '''
    sys.exit(app.exec_())
