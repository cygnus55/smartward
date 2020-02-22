import sys
import matplotlib
import dbconnect
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

db=dbconnect.database_statwindow('localhost','root')

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class StatWindow(QtWidgets.QMainWindow):
    def __init__(self,name,table_name,*args, **kwargs):
        super(StatWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("{} Statistics".format(name))
        self.setFixedSize(900,600)
        
        sc = MplCanvas(self, width=5, height=4, dpi=100)

        def plot_year():
            print("Year")
            x_axis=list(range(1,11))
            x__axis=['2067/%','2068/%','2069/%',"2070/%",'2071/%','2072/%','2073/%','2074/%','2075/%','2076/%']
            y_axis=[]
            for x in x__axis:
                y_axis.append(db.getRowCount('RegDate',table_name,x))
            
            print(y_axis)
            sc.axes.cla
            sc.axes.plot(x_axis,y_axis)
            sc.axes.set_title("{0} by {1}".format(name,"Year"))
            sc.axes.set_xlabel("Year")
            sc.axes.set_ylabel("No. of {}".format(name))
       
        def plot_month():
            print("Month")
            x_axis=list(range(1,13))
            x__axis=["2076/01/%",'2076/02/%','2076/03/%','2076/04/%','2076/05/%',"2076/06/%",'2076/07/%','2076/08/%','2076/09/%','2076/10/%','2076/11/%','2076/12/%']
            y_axis=[]
            for x in x__axis:
                y_axis.append(db.getRowCount('RegDate',table_name,x))
            
            print(y_axis)
            sc.axes.cla
            sc.axes.plot(x_axis,y_axis)
            sc.axes.set_title("{0} by {1}".format(name,"Month"))
            sc.axes.set_xlabel("Month")
            sc.axes.set_ylabel("No. of {}".format(name))

        def plot_day():
            print("Day")
            x_axis=list(range(1,32))
            x__axis=[]
            for x in x_axis:
                x__axis.append('2076/11/{}'.format(str(x)))
            print(x__axis)
            y_axis=[]
            for x in x__axis:
                y_axis.append(db.getRowCount('RegDate',table_name,x))
            
            print(y_axis)
            sc.axes.cla
            sc.axes.plot(x_axis,y_axis)
            sc.axes.set_title("{0} by {1}".format(name,"Day"))
            sc.axes.set_xlabel("Day")
            sc.axes.set_ylabel("No. of {}".format(name))
        
        def change_parameter():
            parameter=self.dropdown.currentText()
            if parameter=="Year":
                plot_year()
            elif parameter=="Month":
                plot_month()
            elif parameter=="Day":
                plot_day()
               
                
        self.dropdown=QtWidgets.QComboBox(sc)
        self.dropdown.setGeometry(QtCore.QRect(0,0,200,30))
        self.dropdown.addItem('Month')        
        self.dropdown.addItem('Day')
        self.dropdown.addItem('Year')
        self.dropdown.setObjectName('dropdown')
        self.dropdown.currentTextChanged.connect(change_parameter)
        
        plot_year()
        self.setCentralWidget(sc)

        self.show()
    

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = StatWindow("Death","deathregistration")
    app.exec_()
