from PyQt5 import QtWidgets,QtCore,QtGui
from ui_gharbato import *

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)

    name=ui.nameLineEdit.text()
    p_address=ui.permanentAddressLineEdit.text()
    add_malpot=ui.addressOfMalpotLineEdit.text()
    citizenship_num=ui.citizenshipNoLineEdit.text()

    def on_submit_clicked():
        #connection with database and sending values to table(incomplete)

        #checking the values returned (empty)(incomplete) 

        print("Name: {}".format(name))
        print("Permanent address: {}".format(p_address))
        print("Address of malpot office {}".format(add_malpot))
        print("Citizenship no.: {}".format(citizenship_num))
        
        #generating text files from the data given(incomplete)

        filename="{0}_gharbato.txt".format(name)
        
        with open(filename,'w') as doc:
            doc.write() #write content from the text file
        doc.close()

    ui.pushButton_submit.clicked.connect(on_submit_clicked)




    mainWindow.show()
    
    
    
    
    
    sys.exit(app.exec_())