# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_secondwindow(object):
    def open():
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_secondwindow()
        self.ui.setupUi(self.window)
        self.window.close()
 
        
    
        
    
    def setupUi(self, secondwindow):
        secondwindow.setObjectName("secondwindow")
        secondwindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(secondwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 190, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.open)
        secondwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(secondwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        secondwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(secondwindow)
        self.statusbar.setObjectName("statusbar")
        secondwindow.setStatusBar(self.statusbar)

        self.retranslateUi(secondwindow)
        QtCore.QMetaObject.connectSlotsByName(secondwindow)

    def retranslateUi(self, secondwindow):
        _translate = QtCore.QCoreApplication.translate
        secondwindow.setWindowTitle(_translate("secondwindow", "MainWindow"))
        self.pushButton.setText(_translate("secondwindow", "clicked"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    secondwindow = QtWidgets.QMainWindow()
    ui = Ui_secondwindow()
    ui.setupUi(secondwindow)
    secondwindow.show()
    sys.exit(app.exec_())

