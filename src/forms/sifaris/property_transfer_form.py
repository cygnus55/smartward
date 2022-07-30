from PyQt5 import QtCore, QtGui, QtWidgets
from ui_propertytransferform import *

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    name_of_holder=ui.fullNameLineEdit.text()
    date=ui.dateOfDeathDateEdit.text()
    kitta_num=ui.kitaNoLineEdit.text()
    name_of_receiver=ui.nameLineEdit.text()
    relation=ui.relationWithDeceisedComboBox.currentText()

    def on_submit_clicked():
        #connection with database and sending values to table(incomplete)

        #checking the values returned (empty)(incomplete) 

        print("Name of holder: {}".format(name_of_holder))
        print("Date: {}".format(date))
        print("Kitta no.: {}".format(kitta_num))
        print("Name of receiver: {}".format(name_of_receiver))
        print("Relation: {}".format(relation))
        
        #generating text files from the data given(incomplete)

        filename="{0}to{1}.txt".format(name_of_holder,name_of_receiver)
        
        with open(filename,'w') as doc:
            doc.write() #write content from the text file
        doc.close()

    ui.pushButton_submit.clicked.connect(on_submit_clicked)

    sys.exit(app.exec_())
