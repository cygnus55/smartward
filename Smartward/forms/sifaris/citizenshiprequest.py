# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'citizenshiprequestform.ui'
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

table="citizenshipRegistration"



class Ui_CitizenshipRequest(object):
    def setupUi(self, citizenshiprequest):
        citizenshiprequest.setObjectName("citizenshiprequest")
        citizenshiprequest.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(citizenshiprequest)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 755, 779))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.fullNameLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.fullNameLabel.setObjectName("fullNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.fullNameLabel)
        self.fullNameLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.fullNameLineEdit.setObjectName("fullNameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fullNameLineEdit)
        self.genderLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.genderLabel.setObjectName("genderLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.genderLabel)
        self.genderComboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.genderComboBox.setObjectName("genderComboBox")
        self.genderComboBox.addItem("")
        self.genderComboBox.addItem("")
        self.genderComboBox.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.genderComboBox)
        self.birthPlaceLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.birthPlaceLabel.setObjectName("birthPlaceLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.birthPlaceLabel)
        self.birthPlaceLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.birthPlaceLineEdit.setObjectName("birthPlaceLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.birthPlaceLineEdit)
        self.permanentAdressLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.permanentAdressLabel.setObjectName("permanentAdressLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.permanentAdressLabel)
        self.districtLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.districtLabel.setObjectName("districtLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.districtLabel)
        self.districtLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit.setObjectName("districtLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.districtLineEdit)
        self.MunicipalityLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.MunicipalityLabel.setObjectName("MunicipalityLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.MunicipalityLabel)
        self.MunicipalityLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.MunicipalityLineEdit.setObjectName("MunicipalityLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.MunicipalityLineEdit)
        self.wardNoLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.wardNoLabel.setObjectName("wardNoLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.wardNoLabel)
        self.wardNoLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.wardNoLineEdit.setObjectName("wardNoLineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.wardNoLineEdit)
        self.dateOfBirthLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.dateOfBirthLabel.setObjectName("dateOfBirthLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.dateOfBirthLabel)
        self.dateOfBirthDateEdit = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        self.dateOfBirthDateEdit.setObjectName("dateOfBirthDateEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.dateOfBirthDateEdit)
        self.fathersSDetailLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.fathersSDetailLabel.setObjectName("fathersSDetailLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.fathersSDetailLabel)
        self.fullNameLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.fullNameLabel_2.setObjectName("fullNameLabel_2")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.fullNameLabel_2)
        self.fullNameLineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.fullNameLineEdit_2.setObjectName("fullNameLineEdit_2")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.fullNameLineEdit_2)
        self.adresssLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.adresssLabel.setObjectName("adresssLabel")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.adresssLabel)
        self.adresssLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.adresssLineEdit.setObjectName("adresssLineEdit")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.adresssLineEdit)
        self.citizenshipNoLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.citizenshipNoLabel.setObjectName("citizenshipNoLabel")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.citizenshipNoLabel)
        self.citizenshipNoLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.citizenshipNoLineEdit.setObjectName("citizenshipNoLineEdit")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.citizenshipNoLineEdit)
        self.motherSDetailLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.motherSDetailLabel.setObjectName("motherSDetailLabel")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.motherSDetailLabel)
        self.fullNameLabel_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.fullNameLabel_3.setObjectName("fullNameLabel_3")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.fullNameLabel_3)
        self.fullNameLineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.fullNameLineEdit_3.setObjectName("fullNameLineEdit_3")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.fullNameLineEdit_3)
        self.adrdessLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.adrdessLabel.setObjectName("adrdessLabel")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.adrdessLabel)
        self.adrdessLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.adrdessLineEdit.setObjectName("adrdessLineEdit")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.adrdessLineEdit)
        self.citizenshipNoLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.citizenshipNoLabel_2.setObjectName("citizenshipNoLabel_2")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.citizenshipNoLabel_2)
        self.citizenshipNoLineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.citizenshipNoLineEdit_2.setObjectName("citizenshipNoLineEdit_2")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.citizenshipNoLineEdit_2)
        self.husbandWifeDetailsLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.husbandWifeDetailsLabel.setObjectName("husbandWifeDetailsLabel")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.husbandWifeDetailsLabel)
        self.fullNameLabel_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.fullNameLabel_4.setObjectName("fullNameLabel_4")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.fullNameLabel_4)
        self.fullNameLineEdit_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.fullNameLineEdit_4.setObjectName("fullNameLineEdit_4")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.fullNameLineEdit_4)
        self.addressLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.addressLabel.setObjectName("addressLabel")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.LabelRole, self.addressLabel)
        self.addressLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.addressLineEdit.setObjectName("addressLineEdit")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.FieldRole, self.addressLineEdit)
        self.citizenshipNoLabel_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.citizenshipNoLabel_3.setObjectName("citizenshipNoLabel_3")
        self.formLayout.setWidget(19, QtWidgets.QFormLayout.LabelRole, self.citizenshipNoLabel_3)
        self.citizenshipNoLineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.citizenshipNoLineEdit_3.setObjectName("citizenshipNoLineEdit_3")
        self.formLayout.setWidget(19, QtWidgets.QFormLayout.FieldRole, self.citizenshipNoLineEdit_3)
        self.detailsOfGuardianLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.detailsOfGuardianLabel.setObjectName("detailsOfGuardianLabel")
        self.formLayout.setWidget(20, QtWidgets.QFormLayout.LabelRole, self.detailsOfGuardianLabel)
        self.fullNameLabel_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.fullNameLabel_5.setObjectName("fullNameLabel_5")
        self.formLayout.setWidget(21, QtWidgets.QFormLayout.LabelRole, self.fullNameLabel_5)
        self.fullNameLineEdit_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.fullNameLineEdit_5.setObjectName("fullNameLineEdit_5")
        self.formLayout.setWidget(21, QtWidgets.QFormLayout.FieldRole, self.fullNameLineEdit_5)
        self.addressLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.addressLabel_2.setObjectName("addressLabel_2")
        self.formLayout.setWidget(22, QtWidgets.QFormLayout.LabelRole, self.addressLabel_2)
        self.addressLineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.addressLineEdit_2.setObjectName("addressLineEdit_2")
        self.formLayout.setWidget(22, QtWidgets.QFormLayout.FieldRole, self.addressLineEdit_2)
        self.gridLayout_2.addLayout(self.formLayout, 2, 0, 1, 1)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.registrationNoLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.registrationNoLabel.setObjectName("registrationNoLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.registrationNoLabel)
        self.registrationNoLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.registrationNoLineEdit.setObjectName("registrationNoLineEdit")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.registrationNoLineEdit)
        self.gridLayout_2.addLayout(self.formLayout_3, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.scrollAreaWidgetContents)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 3, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        citizenshiprequest.setCentralWidget(self.centralwidget)

        self.retranslateUi(citizenshiprequest)
        QtCore.QMetaObject.connectSlotsByName(citizenshiprequest)

    def retranslateUi(self, citizenshiprequest):
        _translate = QtCore.QCoreApplication.translate
        citizenshiprequest.setWindowTitle(_translate("citizenshiprequest", "Nepali Citizenship Request"))
        self.fullNameLabel.setText(_translate("citizenshiprequest", "Full Name"))
        self.genderLabel.setText(_translate("citizenshiprequest", "Gender"))
        self.genderComboBox.setItemText(0, _translate("citizenshiprequest", "Male"))
        self.genderComboBox.setItemText(1, _translate("citizenshiprequest", "Female"))
        self.genderComboBox.setItemText(2, _translate("citizenshiprequest", "Other"))
        self.birthPlaceLabel.setText(_translate("citizenshiprequest", "Birth place"))
        self.permanentAdressLabel.setText(_translate("citizenshiprequest", "<b>Permanent Address</b>"))
        self.districtLabel.setText(_translate("citizenshiprequest", "District"))
        self.MunicipalityLabel.setText(_translate("citizenshiprequest", "Rural Municipality/Municipality"))
        self.wardNoLabel.setText(_translate("citizenshiprequest", "Ward No"))
        self.dateOfBirthLabel.setText(_translate("citizenshiprequest", "Date Of Birth"))
        self.fathersSDetailLabel.setText(_translate("citizenshiprequest", "<b>Fathers\'s Details</b>"))
        self.fullNameLabel_2.setText(_translate("citizenshiprequest", "Full Name"))
        self.adresssLabel.setText(_translate("citizenshiprequest", "Addresss"))
        self.citizenshipNoLabel.setText(_translate("citizenshiprequest", "Citizenship No"))
        self.motherSDetailLabel.setText(_translate("citizenshiprequest", "<b>Mother\'s Details</b>"))
        self.fullNameLabel_3.setText(_translate("citizenshiprequest", "Full Name"))
        self.adrdessLabel.setText(_translate("citizenshiprequest", "Adrdess"))
        self.citizenshipNoLabel_2.setText(_translate("citizenshiprequest", "Citizenship No"))
        self.husbandWifeDetailsLabel.setText(_translate("citizenshiprequest", "Husband/Wife Details"))
        self.fullNameLabel_4.setText(_translate("citizenshiprequest", "Full Name"))
        self.addressLabel.setText(_translate("citizenshiprequest", "Address"))
        self.citizenshipNoLabel_3.setText(_translate("citizenshiprequest", "Citizenship No"))
        self.detailsOfGuardianLabel.setText(_translate("citizenshiprequest", "<b>Details Of Guardian</b>"))
        self.fullNameLabel_5.setText(_translate("citizenshiprequest", "Full Name"))
        self.addressLabel_2.setText(_translate("citizenshiprequest", "Address"))
        self.registrationNoLabel.setText(_translate("citizenshiprequest", "Registration no"))
        self.label.setText(_translate("citizenshiprequest", "<b>Details Of Candidate</b>"))

class ActualWork():
    def __init__(self):
        import dbconnect
        self.db=dbconnect.database_wardwindow("localhost","root")
        self.citizenshipForm = QtWidgets.QMainWindow()
        self.ui = Ui_CitizenshipRequest()
        self.ui.setupUi(self.citizenshipForm)
        self.citizenshipForm.show()
        self.actualWork()

    def actualWork(self):
        self.ui.buttonBox.accepted.connect(self.submitform)
        self.ui.buttonBox.rejected.connect(lambda:self.citizenshipForm.close())

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
        self.citizenRegNo=self.ui.registrationNoLineEdit.text()
        date=QDate(self.ui.dateOfBirthDateEdit.date())
        year,month,day=date.getDate()
        birth_in_ad=datetime.date(year,month,day)
        birth_in_bs=nepali_date.NepaliDate.to_nepali_date(birth_in_ad)
        #registration date
        today=nepali_date.NepaliDate.today()
        registrationdate=str(today)[3:]
        #birth date
        self.birthdate=(str(birth_in_ad),str(birth_in_bs)[3:])
        #detailsofcandidate
        detailsofcandidate=(self.birthdate,self.ui.fullNameLineEdit.text(),self.ui.genderComboBox.currentText(),self.ui.birthPlaceLineEdit.text(),self.ui.districtLineEdit.text(),self.ui.MunicipalityLineEdit.text(),self.ui.wardNoLineEdit.text())
        #father details
        self.fatherdetail=(self.ui.fullNameLineEdit_2.text(),self.ui.adresssLineEdit.text(),self.ui.citizenshipNoLineEdit.text())
        #motherdetail
        self.motherdetail=(self.ui.fullNameLineEdit_3.text(),self.ui.adrdessLineEdit.text(),self.ui.citizenshipNoLineEdit_2.text())
        #parent detail
        parentdetail=(self.fatherdetail,self.motherdetail)
        #husband/wife detail
        husbandorwifedetail=(self.ui.fullNameLineEdit_4.text(),self.ui.addressLineEdit.text(),self.ui.citizenshipNoLineEdit_3.text())
        #localguardian details
        localguardian=(self.ui.fullNameLineEdit_5.text(),self.ui.addressLineEdit_2.text())
        return {"RegDate":registrationdate,"RegNo":self.citizenRegNo,"detailsofcandidate":str(detailsofcandidate) , "parentdetail":str(parentdetail) , 'detailsofspouse':str(husbandorwifedetail),'detailsoflocalguardian':str(localguardian)}

    def closeActualWork(self):
        self.citizenshipForm.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aw=ActualWork()
    '''
    citizenshiprequest = QtWidgets.QMainWindow()
    ui = Ui_citizenshiprequest()
    ui.setupUi(citizenshiprequest)
    citizenshiprequest.show()
    '''
    sys.exit(app.exec_())
