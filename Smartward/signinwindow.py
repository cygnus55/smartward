from ui_signinwindow import *

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_SigninWindow()
    ui.setupUi(MainWindow)
    ui.mun_logo.setEchoMode(0)
    # Application start to run
    MainWindow.show()   
    sys.exit(app.exec_())

