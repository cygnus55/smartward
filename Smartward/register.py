from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    username="root",
    password="",
    database="smartward"    
    )
#mycursor=mydb.cursor()


class Ui_Dialog(object):
    def register(self):
        name="Ward no. "+self.wada_name.text().strip()
        address=self.wada_address.text().title().strip()
        about=self.wada_info.toPlainText().strip()
        mycursor=mydb.cursor()
        sql="INSERT INTO wada(wada_name,wada_address,wada_info) VALUES (%s,%s,%s)"
        val=(name,address,about)  
        mycursor.execute(sql,val)        
        mydb.commit()
        print("Registration successful.")
        mycursor.close()
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(519, 400)
        
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(150, 20, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 120, 101, 21))
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 160, 81, 31))
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 230, 81, 41))
        self.label_3.setObjectName("label_3")

        self.wada_name = QtWidgets.QLineEdit(Dialog)
        self.wada_name.setGeometry(QtCore.QRect(210, 110, 211, 41))
        self.wada_name.setObjectName("wada_name")
        
        self.wada_address = QtWidgets.QLineEdit(Dialog)
        self.wada_address.setGeometry(QtCore.QRect(210, 160, 211, 41))
        self.wada_address.setObjectName("wada_address")

        self.wada_info = QtWidgets.QTextEdit(Dialog)
        self.wada_info.setGeometry(QtCore.QRect(210, 220, 211, 101))
        self.wada_info.setObjectName("wada_info")
        
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(210, 330, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.register)
        
       
        
        
        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "REGISTER"))
        self.pushButton.setText(_translate("Dialog", "REGISTER"))
        self.label.setText(_translate("Dialog", "WARD NO."))
        self.label_2.setText(_translate("Dialog", "ADDRESS"))
        self.label_3.setText(_translate("Dialog", "ABOUT"))
        self.label_4.setText(_translate("Dialog", " WADA REGISTER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
