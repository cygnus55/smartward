from ui_mainwindow import Ui_WardWindow
from ui_signinwindow import Ui_SigninWindow
from PyQt5.QtWidgets import QApplication,QMainWindow
import pickle

if __name__=="__main__":
    import sys
    app = QApplication(sys.argv)
    
    try:
        with open('ward.pickle','rb') as obj:
            read = pickle.load(obj)
            WardWindow = QMainWindow()
            ui_ward = Ui_WardWindow()
            ui_ward.setupUi(WardWindow)
            WardWindow.show()
    except FileNotFoundError:
        SigninWindow = QMainWindow()
        ui_signin = Ui_SigninWindow()
        ui_signin.setupUi(SigninWindow)
        SigninWindow.show()

    sys.exit(app.exec_())