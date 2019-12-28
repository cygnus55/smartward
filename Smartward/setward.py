from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    username="user",
    password="",
    database="smartward"
    )
wardname=[]
mycursor=mydb.cursor()
sql="SELECT * from wada"
mycursor.execute(sql)
records=mycursor.fetchall()
for row in records:
    wardname.append(row[1])
#print(wardname)
mycursor.close()
    

    

class Ui_Dialog(object):
    def setWard(self):
        name=self.lineEdit.text()
        mycursor=mydb.cursor(buffered=True)
        sql="SELECT * FROM wada WHERE wada_name=%s"
        mycursor.execute(sql,(name,))
        records=mycursor.fetchall()
        #print(mycursor.rowcount)
        for row in records:
            sql="UPDATE wada SET current ='1' WHERE wada_name=%s"                        
            mycursor.execute(sql,(name,))            
        mydb.commit()
        print("Current ward :",row[1])
        sql="SELECT * FROM wada WHERE wada_name!=%s"
        mycursor.execute(sql,(name,))
        records=mycursor.fetchall()
        #print(mycursor.rowcount)
        for row in records:           
            sql="UPDATE wada SET current ='0' WHERE wada_name!=%s"            
            mycursor.execute(sql,(name,))
        mydb.commit()
        mycursor.close()
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(552, 404)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 30, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 140, 41, 31))
        self.label_2.setObjectName("label_2")

        completer=QtWidgets.QCompleter(sorted(wardname))
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(140, 140, 241, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setCompleter(completer)

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(310, 260, 141, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.setWard)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SetWard"))
        self.label.setText(_translate("Dialog", " Set Ward"))
        self.label_2.setText(_translate("Dialog", "NAME:"))
        self.pushButton.setText(_translate("Dialog", "Set"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
