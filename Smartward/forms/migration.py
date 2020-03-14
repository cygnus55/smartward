from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import datetime
import nepali_date
import sw_string
import pickle
from sw_pdf import MigrationCertificate

table = "MigrationRegistration"


class Ui_migration(QWidget):
    def setupUi(self, migration):
        migration.setObjectName("migration")
        migration.resize(888, 989)
        self.centralwidget = QtWidgets.QWidget(migration)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -227, 780, 852))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.registrationNoLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.registrationNoLabel.setObjectName("registrationNoLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.registrationNoLabel)
        self.registrationNoLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.registrationNoLineEdit.setObjectName("registrationNoLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.registrationNoLineEdit)
        self.districtLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.districtLabel_2.setObjectName("districtLabel_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.districtLabel_2)
        self.districtLineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_2.setObjectName("districtLineEdit_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.districtLineEdit_2)
        self.municipalityLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.municipalityLabel_2.setObjectName("municipalityLabel_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.municipalityLabel_2)
        self.municipalityLineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.municipalityLineEdit_2.setObjectName("municipalityLineEdit_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.municipalityLineEdit_2)
        self.wardNoLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.wardNoLabel_2.setObjectName("wardNoLabel_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.wardNoLabel_2)
        self.wardNoLineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.wardNoLineEdit_2.setObjectName("wardNoLineEdit_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.wardNoLineEdit_2)
        self.roadStreetLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.roadStreetLabel_2.setObjectName("roadStreetLabel_2")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.roadStreetLabel_2)
        self.roadStreetLineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.roadStreetLineEdit_2.setObjectName("roadStreetLineEdit_2")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.roadStreetLineEdit_2)
        self.houseNoLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.houseNoLabel_2.setObjectName("houseNoLabel_2")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.houseNoLabel_2)
        self.houseNoLineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.houseNoLineEdit_2.setObjectName("houseNoLineEdit_2")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.houseNoLineEdit_2)
        self.villageCommunityLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.villageCommunityLabel.setObjectName("villageCommunityLabel")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.villageCommunityLabel)
        self.villageCommunityLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.villageCommunityLineEdit.setObjectName("villageCommunityLineEdit")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.villageCommunityLineEdit)
        self.nameOfHomeownerWhoRelocatedLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.nameOfHomeownerWhoRelocatedLabel.setObjectName("nameOfHomeownerWhoRelocatedLabel")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.nameOfHomeownerWhoRelocatedLabel)
        self.nameOfHomeownerWhoRelocatedLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.nameOfHomeownerWhoRelocatedLineEdit.setObjectName("nameOfHomeownerWhoRelocatedLineEdit")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.nameOfHomeownerWhoRelocatedLineEdit)
        self.dateOfRelocatedLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.dateOfRelocatedLabel.setObjectName("dateOfRelocatedLabel")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.dateOfRelocatedLabel)
        self.dateOfRelocatedDateEdit = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        self.dateOfRelocatedDateEdit.setObjectName("dateOfRelocatedDateEdit")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.dateOfRelocatedDateEdit)
        self.reasonOfRelocatedLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.reasonOfRelocatedLabel.setObjectName("reasonOfRelocatedLabel")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.reasonOfRelocatedLabel)
        self.reasonOfRelocatedComboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.reasonOfRelocatedComboBox.setObjectName("reasonOfRelocatedComboBox")
        self.reasonOfRelocatedComboBox.addItem("")
        self.reasonOfRelocatedComboBox.addItem("")
        self.reasonOfRelocatedComboBox.addItem("")
        self.reasonOfRelocatedComboBox.addItem("")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.reasonOfRelocatedComboBox)
        self.gridLayout_2.addLayout(self.formLayout_2, 4, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.setColumnWidth(0,150)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setColumnWidth(1, 250)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setColumnWidth(3, 250)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setColumnWidth(4, 100)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setColumnWidth(5, 200)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.setColumnWidth(6, 200)
        self.tableWidget.setFixedHeight(150)

        self.gridLayout_2.addWidget(self.tableWidget, 6, 0, 1, 1)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.registrationNoLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.registrationNoLabel_2.setObjectName("registrationNoLabel_2")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.registrationNoLabel_2)
        self.registrationNoLineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.registrationNoLineEdit_2.setObjectName("registrationNoLineEdit_2")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.registrationNoLineEdit_2)
        self.familyRecordFormNoLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.familyRecordFormNoLabel.setObjectName("familyRecordFormNoLabel")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.familyRecordFormNoLabel)
        self.familyRecordFormNoLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.familyRecordFormNoLineEdit.setObjectName("familyRecordFormNoLineEdit")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.familyRecordFormNoLineEdit)
        self.gridLayout_2.addLayout(self.formLayout_4, 0, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.districtLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.districtLabel.setObjectName("districtLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.districtLabel)
        self.districtLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit.setObjectName("districtLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.districtLineEdit)
        self.municipalityLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.municipalityLabel.setObjectName("municipalityLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.municipalityLabel)
        self.municipalityLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.municipalityLineEdit.setObjectName("municipalityLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.municipalityLineEdit)
        self.wardNoLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.wardNoLabel.setObjectName("wardNoLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.wardNoLabel)
        self.wardNoLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.wardNoLineEdit.setObjectName("wardNoLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.wardNoLineEdit)
        self.roadStreetLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.roadStreetLabel.setObjectName("roadStreetLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.roadStreetLabel)
        self.roadStreetLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.roadStreetLineEdit.setObjectName("roadStreetLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.roadStreetLineEdit)
        self.houseNoLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.houseNoLabel.setObjectName("houseNoLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.houseNoLabel)
        self.houseNoLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.houseNoLineEdit.setObjectName("houseNoLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.houseNoLineEdit)
        self.villageLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.villageLabel.setObjectName("villageLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.villageLabel)
        self.villageyLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.villageyLineEdit.setObjectName("villageyLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.villageyLineEdit)
        self.gridLayout_2.addLayout(self.formLayout, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.scrollAreaWidgetContents)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 8, 0, 1, 1)
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.InformationProvidedByLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.InformationProvidedByLabel.setObjectName("InformationProvidedByLabel")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.InformationProvidedByLabel)
        self.nameLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.citizenshipCertificateNoLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.citizenshipCertificateNoLabel.setObjectName("citizenshipCertificateNoLabel")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.citizenshipCertificateNoLabel)
        self.citizenshipCertificateNoLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.citizenshipCertificateNoLineEdit.setObjectName("citizenshipCertificateNoLineEdit")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.citizenshipCertificateNoLineEdit)
        self.gridLayout_2.addLayout(self.formLayout_5, 7, 0, 1, 1)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.bDetailsOfThePersonRelocatedLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.bDetailsOfThePersonRelocatedLabel.setObjectName("bDetailsOfThePersonRelocatedLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.bDetailsOfThePersonRelocatedLabel)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.addMore = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.addMore.setText("")
        self.addMore.setObjectName("addMore")
        self.horizontalLayout_4.addWidget(self.addMore)
        self.formLayout_3.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.gridLayout_2.addLayout(self.formLayout_3, 5, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        migration.setCentralWidget(self.centralwidget)

        self.addMore.setText("Add")
        self.addMore.clicked.connect(self.addMoreDetail)
        self.retranslateUi(migration)
        QtCore.QMetaObject.connectSlotsByName(migration)

    def addMoreDetail(self):
        i=self.tableWidget.rowCount()
        self.tableWidget.insertRow(i)


    def retranslateUi(self, migration):
        _translate = QtCore.QCoreApplication.translate
        migration.setWindowTitle(_translate("migration", "Migration Registration Form"))
        self.label_2.setText(_translate("migration", "<b>Place of Origin:</b>"))
        self.registrationNoLabel.setText(_translate("migration", "Registration No"))
        self.districtLabel_2.setText(_translate("migration", "District"))
        self.municipalityLabel_2.setText(_translate("migration", "Municipality"))
        self.wardNoLabel_2.setText(_translate("migration", "Ward No"))
        self.roadStreetLabel_2.setText(_translate("migration", "Road/Street"))
        self.houseNoLabel_2.setText(_translate("migration", "House No"))
        self.villageCommunityLabel.setText(_translate("migration", "Village/Community"))
        self.nameOfHomeownerWhoRelocatedLabel.setText(_translate("migration", "Name of homeowner who relocated"))
        self.dateOfRelocatedLabel.setText(_translate("migration", "Date of relocation"))
        self.reasonOfRelocatedLabel.setText(_translate("migration", "Reason of relocation"))
        self.reasonOfRelocatedComboBox.setItemText(0, _translate("migration", "Job"))
        self.reasonOfRelocatedComboBox.setItemText(1, _translate("migration", "Bussiness"))
        self.reasonOfRelocatedComboBox.setItemText(2, _translate("migration", "New house"))
        self.reasonOfRelocatedComboBox.setItemText(3, _translate("migration", "Other"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("migration", "Birth certificate no."))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("migration", "Full Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("migration", "Gender"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("migration", "Citizenship No."))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("migration", "Issue date"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("migration", "Issue District"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("migration", "Relation with informer"))
        self.registrationNoLabel_2.setText(_translate("migration", "<b>Registration No</b>"))
        self.familyRecordFormNoLabel.setText(_translate("migration", "<b>Family Record Form No"))
        self.districtLabel.setText(_translate("migration", "District"))
        self.municipalityLabel.setText(_translate("migration", "Municipality"))
        self.wardNoLabel.setText(_translate("migration", "Ward No"))
        self.roadStreetLabel.setText(_translate("migration", "Road/Street"))
        self.houseNoLabel.setText(_translate("migration", "House No"))
        self.villageLabel.setText(_translate("migration", "Village/Community"))
        self.label.setText(_translate("migration", "<b>Place of Destination:</b>"))
        self.InformationProvidedByLabel.setText(_translate("migration", "<b>Information Provided By"))
        self.nameLabel.setText(_translate("migration", "Name"))
        self.citizenshipCertificateNoLabel.setText(_translate("migration", "Citizenship Certificate No."))
        self.bDetailsOfThePersonRelocatedLabel.setText(_translate("migration", "<b>Details Of The Person Relocated"))


class ActualWork():
    def __init__(self):
        import dbconnect
        self.db = dbconnect.database_wardwindow("localhost", "root")
        self.MigrationForm = QtWidgets.QMainWindow()
        self.ui = Ui_migration()
        self.ui.setupUi(self.MigrationForm)
        self.MigrationForm.show()
        self.actualWork()

    def actualWork(self):
        self.ui.buttonBox.accepted.connect(self.submitform)
        self.ui.buttonBox.rejected.connect(lambda: self.MigrationForm.close())

    def submitform(self):
        self.values = self.getallvalues()
        a = sw_string.generateList(**self.values)
        # a=["RegDate","1","RegNo","2","C","3","D","4","E","5"]
        # b=['RegNo','123-32','detailsofmarriage', "('Social Tradition', ('2000-01-01', '2056/09/17'))", 'locationofmarriage', "('Kavre', 'Namobudda', '04', 'Timal Road', 'Methinkot', '45', '')", 'detailsofspouse', "{'detailsofbride': ('Tandon', 'Rabina', '2057/01/05', 'Kami', '+2', 'Actress', 'Divorcee', ('Rampur', 'Narayanghat', '5', 'Ghandi Street', 'Hariharpur', '78', 'India'), ('India', '27-12398721', '2071/06/09', 'Rampur', '87289398', 'India', 'New Delhi'), ('Fariha Tandon', 'Kanod Tandon', 'Kajol Tandon')), 'detailsofbridegroom': ('Ghimere', 'Tilak', '2051/03/21', 'Brahmin', 'B.Sc.', 'Astrologer', 'Single', ('Solukhumbu', 'Namche Bazar', '9', 'Manila Street', 'Vaisepati', '567', 'Nepal'), ('Nepal', '983-3468', '2067/03/05', 'Solukhumbu', '', '', ''), ('Goshnath Ghimere', 'Farilal Ghimere', 'Nabina Ghimere'))}"]
        # a=['RegDate',,b[0],b[1],b[2],b[3].replace("'","__"),b[4],b[5].replace("'","__"),b[6],b[7].replace("'","__")]
        # print(a)
        self.db.createFormTable(table)
        self.db.addColumns(table, a[4], a[6],a[8],a[10],a[12])
        self.db.insertValues(table, a)
        self.getCertificate()

    def getallvalues(self):
        self.migRegNo = self.ui.registrationNoLineEdit_2.text()
        # place of destination
        Destination = (
        self.ui.districtLineEdit.text(), self.ui.municipalityLineEdit.text(), self.ui.wardNoLineEdit.text(),
        self.ui.roadStreetLineEdit.text(), self.ui.houseNoLineEdit.text(), self.ui.villageyLineEdit.text())
        date = QDate(self.ui.dateOfRelocatedDateEdit.date())
        year, month, day = date.getDate()
        reallocated_in_ad = datetime.date(year, month, day)
        reallocated_in_bs = nepali_date.NepaliDate.to_nepali_date(reallocated_in_ad)
        today = nepali_date.NepaliDate.today()
        # registration date
        registrationdate = str(today)[3:]
        # date of reallocated
        self.reallocateddate = (str(reallocated_in_ad), str(reallocated_in_bs)[3:])
        # details  of place of origin
        placeoforigin = (
        self.ui.registrationNoLineEdit.text(), self.ui.districtLineEdit_2.text(), self.ui.municipalityLineEdit_2.text(),
        self.ui.wardNoLineEdit_2.text(), self.ui.roadStreetLineEdit_2.text(), self.ui.houseNoLineEdit_2.text(),
        self.ui.villageCommunityLineEdit.text(), self.ui.nameOfHomeownerWhoRelocatedLineEdit.text(),
        self.reallocateddate, self.ui.reasonOfRelocatedComboBox.currentText())

        rows=self.ui.tableWidget.rowCount()
        cols=self.ui.tableWidget.columnCount()
        detailsofmigrants=[['Birth Certificate','Full Name','Gender','Citizenship No.','Issue Date','Issue District','Relation with Informer']]
        for r in range(0,rows):
            row=[]
            for c in range(0,cols):
                try:
                    i=self.ui.tableWidget.item(r,c)
                    row.append(i.text())
                except AttributeError:
                    i='-'
                    row.append(i)
            detailsofmigrants.append(row)
        tabledata=detailsofmigrants
        informer = str((self.ui.nameLineEdit.text(), self.ui.citizenshipCertificateNoLineEdit.text()))
        body=(
            self.migRegNo,registrationdate,self.ui.familyRecordFormNoLineEdit.text(),informer[0],
            self.ui.nameOfHomeownerWhoRelocatedLineEdit.text(),
            self.ui.wardNoLineEdit_2.text(),self.ui.municipalityLineEdit_2.text(),self.ui.districtLineEdit_2.text(),
            self.ui.wardNoLineEdit.text(), self.ui.municipalityLineEdit.text(), self.ui.districtLineEdit.text(),
            self.reallocateddate[1],self.reallocateddate[0]
        )
        certificate=(body,tabledata)
        self.writePickle(certificate)
        return {"RegDate": registrationdate, "RegNo": self.migRegNo,"FamilyRecordNo":self.ui.familyRecordFormNoLineEdit.text(),
                "detailsofdestination": str(Destination),"detailsofplaceoforigin": str(placeoforigin),"detailsofmigrant":str(detailsofmigrants),"Informer":informer}

    def writePickle(self, d):
        with open("certificate.pickle", "wb") as obj:
            pickle.dump(d, obj)
            obj.close()

    def getCertificate(self):
        QMessageBox.information(self.ui, "Migration Registration","Get Migration Registration Certificate.")
        certificate = MigrationCertificate()
        f = open("certificate.pickle", 'rb')
        cert = pickle.load(f)
        certificate.setBody(cert[0])
        certificate.setTable(cert[1])
        certificate.output()
        QMessageBox.information(self.ui, "Migration Registration", "Migration Registration was Successful.")

    def closeActualWork(self):
        self.MigrationForm.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    aw = ActualWork()
    '''
    migration = QtWidgets.QMainWindow()
    ui = Ui_migration()
    ui.setupUi(migration)
    migration.show()
    '''
    sys.exit(app.exec_())
