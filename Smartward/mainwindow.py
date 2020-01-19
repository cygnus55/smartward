from ui_mainwindow import *

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WardWindow = QtWidgets.QMainWindow()
    ui = Ui_WardWindow()
    ui.setupUi(WardWindow)
    WardWindow.show()
    sys.exit(app.exec_())
