# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'copyofcitizenshipform.ui'
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

table="citizenshipcopyRegistration"



class Ui_Requestforcopyofcitizenship(object):
    def setupUi(self, Requestforcopyofcitizenship):
        Requestforcopyofcitizenship.setObjectName("Requestforcopyofcitizenship")
        Requestforcopyofcitizenship.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Requestforcopyofcitizenship)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 755, 787))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.registrationNoLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.registrationNoLabel.setObjectName("registrationNoLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.registrationNoLabel)
        self.registrationNoLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.registrationNoLineEdit.setObjectName("registrationNoLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.registrationNoLineEdit)
        self.gridLayout_2.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.citizenshipNoLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.citizenshipNoLabel.setObjectName("citizenshipNoLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.citizenshipNoLabel)
        self.citizenshipNoLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.citizenshipNoLineEdit.setObjectName("citizenshipNoLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.citizenshipNoLineEdit)
        self.issueDateLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.issueDateLabel.setObjectName("issueDateLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.issueDateLabel)
        self.issueDateDateEdit = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        self.issueDateDateEdit.setObjectName("issueDateDateEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.issueDateDateEdit)
        self.typeLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.typeLabel.setObjectName("typeLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.typeLabel)
        self.fullNamelabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.fullNamelabel.setObjectName("fullNamelabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.fullNamelabel)
        self.fullNameInLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.fullNameInLineEdit.setObjectName("fullNameInLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.fullNameInLineEdit)
        self.sexLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.sexLabel.setObjectName("sexLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.sexLabel)
        self.sexComboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.sexComboBox.setObjectName("sexComboBox")
        self.sexComboBox.addItem("")
        self.sexComboBox.addItem("")
        self.sexComboBox.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.sexComboBox)
        self.placeOfBirthLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.placeOfBirthLabel.setObjectName("placeOfBirthLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.placeOfBirthLabel)
        self.placeOfBirthLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.placeOfBirthLineEdit.setObjectName("placeOfBirthLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.placeOfBirthLineEdit)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.districtLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.districtLabel.setObjectName("districtLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.districtLabel)
        self.districtLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit.setObjectName("districtLineEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.districtLineEdit)
        self.MunicipaliLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.MunicipaliLabel.setObjectName("MunicipaliLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.MunicipaliLabel)
        self.MunicipalityLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.MunicipalityLineEdit.setObjectName("MunicipalityLineEdit")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.MunicipalityLineEdit)
        self.wardNoLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.wardNoLabel.setObjectName("wardNoLabel")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.wardNoLabel)
        self.wardNoLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.wardNoLineEdit.setObjectName("wardNoLineEdit")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.wardNoLineEdit)
        self.dateOfBirthLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.dateOfBirthLabel.setObjectName("dateOfBirthLabel")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.dateOfBirthLabel)
        self.dateOfBirthDateEdit = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        self.dateOfBirthDateEdit.setObjectName("dateOfBirthDateEdit")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.dateOfBirthDateEdit)
        self.fatherSDetailLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.fatherSDetailLabel.setObjectName("fatherSDetailLabel")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.fatherSDetailLabel)
        self.fullNameLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.fullNameLabel.setObjectName("fullNameLabel")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.fullNameLabel)
        self.fullNameLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.fullNameLineEdit.setObjectName("fullNameLineEdit")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.fullNameLineEdit)
        self.countryLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.countryLabel.setObjectName("countryLabel")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.countryLabel)
        self.countryLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.countryLineEdit.setObjectName("countryLineEdit")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.countryLineEdit)
        self.typesOfCitizenshipLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.typesOfCitizenshipLabel.setObjectName("typesOfCitizenshipLabel")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.typesOfCitizenshipLabel)
        self.motherSDetailLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.motherSDetailLabel.setObjectName("motherSDetailLabel")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.motherSDetailLabel)
        self.fullNameLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.fullNameLabel_2.setObjectName("fullNameLabel_2")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.fullNameLabel_2)
        self.fullNameLineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.fullNameLineEdit_2.setObjectName("fullNameLineEdit_2")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.fullNameLineEdit_2)
        self.typesOfCitizenshipLabel_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.typesOfCitizenshipLabel_4.setObjectName("typesOfCitizenshipLabel_4")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.typesOfCitizenshipLabel_4)
        self.typesOfCitizenshipLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.typesOfCitizenshipLineEdit.setObjectName("typesOfCitizenshipLineEdit")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.typesOfCitizenshipLineEdit)
        self.countryLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.countryLabel_2.setObjectName("countryLabel_2")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.LabelRole, self.countryLabel_2)
        self.countryLineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.countryLineEdit_2.setObjectName("countryLineEdit_2")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.FieldRole, self.countryLineEdit_2)
        self.husbandDetailsLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.husbandDetailsLabel.setObjectName("husbandDetailsLabel")
        self.formLayout.setWidget(19, QtWidgets.QFormLayout.LabelRole, self.husbandDetailsLabel)
        self.fullNmaeLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.fullNmaeLabel.setObjectName("fullNmaeLabel")
        self.formLayout.setWidget(20, QtWidgets.QFormLayout.LabelRole, self.fullNmaeLabel)
        self.fullNmaeLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.fullNmaeLineEdit.setObjectName("fullNmaeLineEdit")
        self.formLayout.setWidget(20, QtWidgets.QFormLayout.FieldRole, self.fullNmaeLineEdit)
        self.countryLabel_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.countryLabel_3.setObjectName("countryLabel_3")
        self.formLayout.setWidget(21, QtWidgets.QFormLayout.LabelRole, self.countryLabel_3)
        self.countryLineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.countryLineEdit_3.setObjectName("countryLineEdit_3")
        self.formLayout.setWidget(21, QtWidgets.QFormLayout.FieldRole, self.countryLineEdit_3)
        self.typesOfCitizenshipLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.typesOfCitizenshipLabel_2.setObjectName("typesOfCitizenshipLabel_2")
        self.formLayout.setWidget(22, QtWidgets.QFormLayout.LabelRole, self.typesOfCitizenshipLabel_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.scrollAreaWidgetContents)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(23, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(22, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.gridLayout_2.addLayout(self.formLayout, 2, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        Requestforcopyofcitizenship.setCentralWidget(self.centralwidget)

        self.retranslateUi(Requestforcopyofcitizenship)
        QtCore.QMetaObject.connectSlotsByName(Requestforcopyofcitizenship)

    def retranslateUi(self, Requestforcopyofcitizenship):
        _translate = QtCore.QCoreApplication.translate
        Requestforcopyofcitizenship.setWindowTitle(_translate("Requestforcopyofcitizenship", "copyof citizenship form"))
        self.label.setText(_translate("Requestforcopyofcitizenship", "Details of the citizenship certificate"))
        self.registrationNoLabel.setText(_translate("Requestforcopyofcitizenship", "Registration no"))
        self.citizenshipNoLabel.setText(_translate("Requestforcopyofcitizenship", "Citizenship No"))
        self.issueDateLabel.setText(_translate("Requestforcopyofcitizenship", "Issue Date"))
        self.typeLabel.setText(_translate("Requestforcopyofcitizenship", "Type"))
        self.fullNamelabel.setText(_translate("Requestforcopyofcitizenship", "Full Name(In BlocK)"))
        self.sexLabel.setText(_translate("Requestforcopyofcitizenship", "Sex"))
        self.sexComboBox.setItemText(0, _translate("Requestforcopyofcitizenship", "Male"))
        self.sexComboBox.setItemText(1, _translate("Requestforcopyofcitizenship", "Femle"))
        self.sexComboBox.setItemText(2, _translate("Requestforcopyofcitizenship", "Other"))
        self.placeOfBirthLabel.setText(_translate("Requestforcopyofcitizenship", "Place of Birth(In Block)"))
        self.label_2.setText(_translate("Requestforcopyofcitizenship", "Permanent Address"))
        self.districtLabel.setText(_translate("Requestforcopyofcitizenship", "District"))
        self.MunicipaliLabel.setText(_translate("Requestforcopyofcitizenship", "Rural Municipality/Municipality"))
        self.wardNoLabel.setText(_translate("Requestforcopyofcitizenship", "Ward No"))
        self.dateOfBirthLabel.setText(_translate("Requestforcopyofcitizenship", "Date Of Birth"))
        self.fatherSDetailLabel.setText(_translate("Requestforcopyofcitizenship", "Father\'s Detail"))
        self.fullNameLabel.setText(_translate("Requestforcopyofcitizenship", "Full Name"))
        self.countryLabel.setText(_translate("Requestforcopyofcitizenship", "Country"))
        self.typesOfCitizenshipLabel.setText(_translate("Requestforcopyofcitizenship", "Types of citizenship"))
        self.motherSDetailLabel.setText(_translate("Requestforcopyofcitizenship", "Mother\'s Detail"))
        self.fullNameLabel_2.setText(_translate("Requestforcopyofcitizenship", "Full Name"))
        self.typesOfCitizenshipLabel_4.setText(_translate("Requestforcopyofcitizenship", "Types of citizenship"))
        self.countryLabel_2.setText(_translate("Requestforcopyofcitizenship", "Country"))
        self.husbandDetailsLabel.setText(_translate("Requestforcopyofcitizenship", "Husband Details"))
        self.fullNmaeLabel.setText(_translate("Requestforcopyofcitizenship", "Full Nmae"))
        self.countryLabel_3.setText(_translate("Requestforcopyofcitizenship", "Country"))
        self.typesOfCitizenshipLabel_2.setText(_translate("Requestforcopyofcitizenship", "Types of citizenship"))
class ActualWork():
    def __init__(self):
        import dbconnect
        self.db=dbconnect.database_wardwindow("localhost","root")
        self.citizencopyForm = QtWidgets.QMainWindow()
        self.ui = Ui_Requestforcopyofcitizenship()
        self.ui.setupUi(self.citizencopyForm)
        self.citizencopyForm.show()
        self.actualWork()

    def actualWork(self):
        self.ui.buttonBox.accepted.connect(self.submitform)
        self.ui.buttonBox.rejected.connect(lambda:self.citizencopyForm.close())

    def submitform(self):
        self.values=self.getallvalues()
        a=sw_string.generateList(**self.values)
        #a=["RegDate","1","RegNo","2","C","3","D","4","E","5"]
        #b=['RegNo','123-32','detailsofmarriage', "('Social Tradition', ('2000-01-01', '2056/09/17'))", 'locationofmarriage', "('Kavre', 'Namobudda', '04', 'Timal Road', 'Methinkot', '45', '')", 'detailsofspouse', "{'detailsofbride': ('Tandon', 'Rabina', '2057/01/05', 'Kami', '+2', 'Actress', 'Divorcee', ('Rampur', 'Narayanghat', '5', 'Ghandi Street', 'Hariharpur', '78', 'India'), ('India', '27-12398721', '2071/06/09', 'Rampur', '87289398', 'India', 'New Delhi'), ('Fariha Tandon', 'Kanod Tandon', 'Kajol Tandon')), 'detailsofbridegroom': ('Ghimere', 'Tilak', '2051/03/21', 'Brahmin', 'B.Sc.', 'Astrologer', 'Single', ('Solukhumbu', 'Namche Bazar', '9', 'Manila Street', 'Vaisepati', '567', 'Nepal'), ('Nepal', '983-3468', '2067/03/05', 'Solukhumbu', '', '', ''), ('Goshnath Ghimere', 'Farilal Ghimere', 'Nabina Ghimere'))}"]
        #a=['RegDate',,b[0],b[1],b[2],b[3].replace("'","__"),b[4],b[5].replace("'","__"),b[6],b[7].replace("'","__")]
        #print(a)
        self.db.createFormTable(table)
        self.db.addColumns(table,a[4],a[6],a[8],a[10])
        self.db.insertValues(table,a)

    def getallvalues(self):
        self.citizencopyRegNo=self.ui.registrationNoLineEdit.text()
        date=QDate(self.ui.issueDateDateEdit.date())
        year,month,day=date.getDate()
        issue_in_ad=datetime.date(year,month,day)
        issue_in_bs=nepali_date.NepaliDate.to_nepali_date(issue_in_ad)
        #registration date
        today=nepali_date.NepaliDate.today()
        registrationdate=str(today)[3:]
        #issue date
        self.issuedate=(str(issue_in_ad),str(issue_in_bs)[3:])
        #birthdate
        date=QDate(self.ui.issueDateDateEdit.date())
        year,month,day=date.getDate()
        birth_in_ad=datetime.date(year,month,day)
        birth_in_bs=nepali_date.NepaliDate.to_nepali_date(birth_in_ad)
        self.birthdate=(str(birth_in_ad),str(birth_in_bs)[3:])
        #details of candidate and related citizenship
        detailsofcandidateandcitizenship=(self.ui.citizenshipNoLineEdit.text(),self.issuedate,self.ui.lineEdit.text(),self.ui.fullNameInLineEdit.text(),self.ui.sexComboBox.currentText(),self.ui.placeOfBirthLineEdit.text(),self.ui.districtLineEdit.text(),self.ui.MunicipalityLineEdit.text(),self.ui.wardNoLineEdit.text(),self.birthdate)
        #details of father
        fatherdetails=(self.ui.fullNameLineEdit.text(),self.ui.countryLineEdit.text(),self.ui.lineEdit_2.text())
        #mother details
        Motherdetails=(self.ui.fullNameLineEdit_2.text(),self.ui.typesOfCitizenshipLineEdit.text(),self.ui.countryLineEdit_2.text())
        #husband or wife details
        husbandorwifedetails=(self.ui.fullNmaeLineEdit.text(),self.ui.countryLineEdit_3.text(),self.ui.lineEdit_3.text())
        return {"RegDate":registrationdate,"RegNo":self.citizencopyRegNo,"detailsofcandiadte":str(detailsofcandidateandcitizenship) , "locationoffather":str(fatherdetails) , 'detailsofmother':str(Motherdetails),'detailsofpartner':str(husbandorwifedetails)}
        

        
    def closeActualWork(self):
        self.citizencopyForm.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aw=ActualWork()
    '''
    Requestforcopyofcitizenship = QtWidgets.QMainWindow()
    ui = Ui_Requestforcopyofcitizenship()
    ui.setupUi(Requestforcopyofcitizenship)
    Requestforcopyofcitizenship.show()
    '''
    sys.exit(app.exec_())
