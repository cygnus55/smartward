from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import datetime
import nepali_date
import sw_string
from sw_pdf import TypeRecommendation

class Ui_TypeReco(QWidget):

    def setupUi(self, TypeReco):
        TypeReco.setObjectName("TypeReco")
        TypeReco.setEnabled(True)
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
        self.pushButton.setGeometry(QtCore.QRect(790, 40, 106, 31))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(15, 114, 886, 16777161))
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
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 80, 881, 27))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.subject = QtWidgets.QLineEdit(self.widget)
        self.subject.setObjectName("subject")
        self.horizontalLayout.addWidget(self.subject)
        TypeReco.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TypeReco)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 921, 22))
        self.menubar.setObjectName("menubar")
        TypeReco.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TypeReco)
        self.statusbar.setObjectName("statusbar")
        TypeReco.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.save)

        self.retranslateUi(TypeReco)
        QtCore.QMetaObject.connectSlotsByName(TypeReco)

    def save(self):
        reco_text = self.textEdit.toPlainText()
        with open('txtfiles/newrecommendation.txt', 'w') as f:
            f.write(reco_text)
            f.close()
        print('file created')
        self.getRecommendation()

    def getRecommendation(self):
        recommendation = TypeRecommendation()
        recommendation.setSubject(self.subject.text())
        recommendation.setBody()
        recommendation.output()
        QMessageBox.information(self, "Recommendation Letter", "Recommendation letter was sucessfully created.")

    def retranslateUi(self, TypeReco):
        _translate = QtCore.QCoreApplication.translate
        TypeReco.setWindowTitle(_translate("TypeReco", "Type Recommendation Letter"))
        self.pushButton.setText(_translate("TypeReco", "Save"))
        self.label.setText(_translate("TypeReco", "<b>Type Recommendation Letter</b>"))
        self.label_2.setText(_translate("TypeReco", "<b>Subject of Recommendation Letter"))


        
'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aw=ActualWork()
    
    TypeReco = QtWidgets.QMainWindow()
    ui = Ui_TypeReco()
    ui.setupUi(TypeReco)
    TypeReco.show()
    
    sys.exit(app.exec_())
    '''