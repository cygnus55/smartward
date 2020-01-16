from PyQt5 import QtCore, QtGui, QtWidgets
from ui_incomesourcerecommendation import *

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
   

    def on_submit_clicked():
    	name=ui.nameLineEdit.text()
    	major_income_source=ui.majorIncomeSourceLineEdit.text()
    	print(name,major_income_source)
        #connect to the database and send the values(incomplete)
        
        #checking the values returned(empty value)(error)
        #print("Name: {0}".format(name))
        #print("Major income Source: {0}".format(major_income_source))

        #generating the text file (incomplete)
        #filename="{}_income_source.txt".format(name)

        #with open(filename,'w') as doc:
        #doc.write() #write the contents in the text file
        #doc.close()

    ui.pushButton_submit.clicked.connect(on_submit_clicked)

    sys.exit(app.exec_())
