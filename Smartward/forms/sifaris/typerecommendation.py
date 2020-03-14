from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import datetime
import nepali_date
import sw_string

class Ui_TypeReco(object):
    def setupUi(self, TypeReco):
        TypeReco.setObjectName("TypeReco")
        TypeReco.resize(921, 728)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TypeReco.sizePolicy().hasHeightForWidth())
        TypeReco.setSizePolicy(sizePolicy)
        TypeReco.setMinimumSize(QtCore.QSize(921, 728))
        TypeReco.setMaximumSize(QtCore.QSize(921, 728))
        TypeReco.setSizeIncrement(QtCore.QSize(-1, 0))
        self.centralwidget = QtWidgets.QWidget(TypeReco)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(15, 15, 106, 31))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(15, 60, 886, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(195, 15, 511, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        TypeReco.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TypeReco)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 921, 21))
        self.menubar.setObjectName("menubar")
        TypeReco.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TypeReco)
        self.statusbar.setObjectName("statusbar")
        TypeReco.setStatusBar(self.statusbar)

        self.retranslateUi(TypeReco)
        QtCore.QMetaObject.connectSlotsByName(TypeReco)

    def retranslateUi(self, TypeReco):
        _translate = QtCore.QCoreApplication.translate
        TypeReco.setWindowTitle(_translate("TypeReco", "Type Recommendation Letter"))
        self.pushButton.setText(_translate("TypeReco", "Save"))
        self.label.setText(_translate("TypeReco", "<b>Type Recommendation Letter</b>"))

class ActualWork():
    def __init__(self):
        self.typerecowindow = QtWidgets.QMainWindow()
        self.ui = Ui_TypeReco()
        self.ui.setupUi(self.typerecowindow)
        self.typerecowindow.show()
        self.ui.pushButton.clicked.connect(self.save)

    def save(self):
        reco_text=self.ui.textEdit.toPlainText()
        print(reco_text)
        print(type(reco_text))
        '''
        with open('output.txt','w+') as f: 
            f.write()
            f.close()
            '''
        print('file created')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aw=ActualWork()
    '''
    TypeReco = QtWidgets.QMainWindow()
    ui = Ui_TypeReco()
    ui.setupUi(TypeReco)
    TypeReco.show()
    '''
    sys.exit(app.exec_())
