import re
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#from PyQt5.QDate import *
from ui_dayscalculator import *
import days_calculator
	
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    DaysCalc = QtWidgets.QMainWindow()
    ui = Ui_DaysCalculator()
    ui.setupUi(DaysCalc)
    DaysCalc.show()
    ui.label_daysCalculator.setText("Days Calculator")
    ui.label_initialDate.setText("Initial Date :-")
    ui.label_finalDate.setText("Final Date :-")
    ui.pushButton_calculate.setText("Calculate")
    ui.pushButton_quit.setText("Quit")
    ui.label_totalDays.setText("")
    minDate=QDate(1900,1,1)
    maxDate=QDate(2100,12,31)
    ui.dateEdit_initialDate.setDisplayFormat("yyyy.MM.dd")
    ui.dateEdit_initialDate.setDate(minDate)
    ui.dateEdit_initialDate.setMinimumDate(minDate)
    ui.dateEdit_initialDate.setMaximumDate(maxDate)
    ui.dateEdit_finalDate.setDisplayFormat("yyyy.MM.dd")
    ui.dateEdit_finalDate.setDate(minDate)
    ui.dateEdit_finalDate.setMinimumDate(minDate)
    ui.dateEdit_finalDate.setMaximumDate(maxDate)
    
    def on_pushButton_calculate_clicked():
    	initial_date=QDate(ui.dateEdit_initialDate.date())
    	final_date=QDate(ui.dateEdit_finalDate.date())
    	y1,m1,d1=initial_date.getDate()
    	y2,m2,d2=final_date.getDate()
    	initial_date={'year': str(y1), 'month': str(m1), 'day': str(d1)}
    	final_date={'year': str(y2), 'month': str(m2), 'day': str(d2)}
    	d1=days_calculator.DaysCalc(initial_date,final_date)
    	ui.label_totalDays.setText("Total Days: "+d1.calc_days())
    	
    def on_pushButton_quit_clicked():
    	sys.exit(app.exec_())
    	
    ui.pushButton_calculate.clicked.connect(on_pushButton_calculate_clicked)
    ui.pushButton_quit.clicked.connect(on_pushButton_quit_clicked)
    
    sys.exit(app.exec_())

