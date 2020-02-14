import sys
import matplotlib
import dbconnect
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

db=dbconnect.database_wardwindow('localhost','root')

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Marriage Statistics")
        # Create the maptlotlib FigureCanvas object, 
        # which defines a single set of axes as self.axes.
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        x_axis=list(range(1,13))
        x__axis=["2076/01/%",'2076/02/%','2076/03/%','2076/04/%','2076/05/%',"2076/06/%",'2076/07/%','2076/08/%','2076/09/%','2076/10/%','2076/11/%','2076/12/%']
        y_axis=[]
        for x in x__axis:
            y_axis.append(db.getRowCount('RegDate','marriageregistration',x))
        #y_axis=list(map(db.getRowCount('RegDate','marriageregistration',f"2076/{x__axis}/%")))
        print(y_axis)
        sc.axes.plot(x_axis,y_axis)
        self.setCentralWidget(sc)

        self.show()
    


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()
