from ui_mainwindow import *

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WardWindow = QtWidgets.QMainWindow()
    ui = Ui_WardWindow()
    ui.setupUi(WardWindow)
    WardWindow.show()

    '''
    Button naming needs consideration
    
    menu=QtWidgets.QMenu()
    menu.addAction(...,...)
    menu.addAction(...,...)
    ui.pushButton.setMenu(menu)
    
    '''


    sys.exit(app.exec_())
