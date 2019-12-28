from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    username="root",
    password="",
    database="smartward"
    )

class Ui_homeWindow(object):
    def refertohome(self):
        self.stackedWidget.setCurrentIndex(0)
        #print("home")
    def refertobirth(self):
        self.stackedWidget.setCurrentIndex(1)
        #print("birth")
    def refertodeath(self):
        self.stackedWidget.setCurrentIndex(2)
        #print("death")
    def refertomarriage(self):
        self.stackedWidget.setCurrentIndex(3)
        #print("marriage")
    def refertodivorce(self):
        self.stackedWidget.setCurrentIndex(4)
        #print("divorce")
        
    def setupUi(self, homeWindow):
        homeWindow.setObjectName("homeWindow")
        homeWindow.resize(1920, 1080)
        homeWindow.setMinimumSize(QtCore.QSize(1920, 1080))
        homeWindow.setMaximumSize(QtCore.QSize(1920, 1080))       
               
        self.centralwidget = QtWidgets.QWidget(homeWindow)
        self.centralwidget.setObjectName("centralwidget")
               
        self.frame_logo = QtWidgets.QFrame(self.centralwidget)
        self.frame_logo.setGeometry(QtCore.QRect(0, 0, 1920, 300))
        self.frame_logo.setStyleSheet("background-color: rgb(170, 0, 127);")
        self.frame_logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_logo.setObjectName("frame_logo")       
        
        mycursor=mydb.cursor(buffered=True)
        sql="SELECT * FROM wada WHERE current=%s"
        val="1"
        mycursor.execute(sql,(val,))
        records=mycursor.fetchall()
        #print(mycursor.rowcount)
        for row in records:
            name=row[1].title()
            address=row[2].title()
            info=row[3]#.capitalize()
            
        logo='logo.png'    
        pixmap=QtGui.QPixmap(logo)
        scaled_pixmap = pixmap.scaled(171, 111, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.label_logo = QtWidgets.QLabel(self.frame_logo)
        self.label_logo.setGeometry(QtCore.QRect(50, 40, 171, 111))
        self.label_logo.setObjectName("label_logo")
        self.label_logo.setPixmap(scaled_pixmap)
        
        self.label_info = QtWidgets.QLabel(self.frame_logo)
        self.label_info.setGeometry(QtCore.QRect(260, 30, 1500, 260))
        self.label_info.setObjectName("label_info")
        self.label_info.setStyleSheet("Color:Black;\n")
        font=QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.label_info.setFont(font)
        self.label_info.setText("Name:     "+name+"\nAddress:  "+address+"\nAbout:    "+info)
        self.label_info.setWordWrap(True)
        #self.label_info.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 300, 1920, 50))
        self.frame.setStyleSheet("background-color: rgb(130, 255, 193);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.pushButton_home= QtWidgets.QPushButton(self.frame)
        self.pushButton_home.setGeometry(QtCore.QRect(10, 0, 93, 51))
        self.pushButton_home.setObjectName("pushButton_home")
        self.pushButton_home.setStyleSheet("color:white;\n""background:blue;\n""border-radius:10px;\n")
        font=QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton_home.setFont(font)
        self.pushButton_home.clicked.connect(self.refertohome)
        
        self.pushButton_birth = QtWidgets.QPushButton(self.frame)
        self.pushButton_birth.setGeometry(QtCore.QRect(140, 0, 93, 51))
        self.pushButton_birth.setObjectName("pushButton_birth")
        self.pushButton_birth.setStyleSheet("color:white;\n""background:blue;\n""border-radius:10px;\n")
        font=QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton_birth.setFont(font)
        self.pushButton_birth.clicked.connect(self.refertobirth)
        
        self.pushButton_death = QtWidgets.QPushButton(self.frame)
        self.pushButton_death.setGeometry(QtCore.QRect(270, 0, 93, 51))
        self.pushButton_death.setObjectName("pushButton_death")
        self.pushButton_death.setStyleSheet("color:white;\n""background:blue;\n""border-radius:10px;\n")
        font=QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton_death.setFont(font)
        self.pushButton_death.clicked.connect(self.refertodeath)
        
        self.pushButton_marriage = QtWidgets.QPushButton(self.frame)
        self.pushButton_marriage.setGeometry(QtCore.QRect(400, 0, 93, 51))
        self.pushButton_marriage.setObjectName("pushButton_marriage")
        self.pushButton_marriage.setStyleSheet("color:white;\n""background:blue;\n""border-radius:10px;\n")
        font=QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton_marriage.setFont(font)
        self.pushButton_marriage.clicked.connect(self.refertomarriage)
        
        self.pushButton_divorce= QtWidgets.QPushButton(self.frame)
        self.pushButton_divorce.setGeometry(QtCore.QRect(530, 0, 93, 51))
        self.pushButton_divorce.setObjectName("pushButton_divorce")
        self.pushButton_divorce.setStyleSheet("color:white;\n""background:blue;\n""border-radius:10px;\n")
        font=QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton_divorce.setFont(font)
        self.pushButton_divorce.clicked.connect(self.refertodivorce)

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 350, 1920, 730))
        self.stackedWidget.setStyleSheet("background:pink;")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stackedWidget.setObjectName("stackedWidget")

        #########################################################################
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.label_info_home=QtWidgets.QLabel(self.home)
        self.label_info_home.setGeometry(QtCore.QRect(10,10,350,40))
        self.label_info_home.setStyleSheet("color:black;\n")
        font=QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        self.label_info_home.setFont(font)
        self.label_info_home.setObjectName("label_info_home")
        self.label_info_home.setText("Home")
        
        
        ############################################################################
        ###########################################################################
        self.stackedWidget.addWidget(self.home)
        self.birth = QtWidgets.QWidget()
        self.birth.setObjectName("birth")
        self.label_info_birth=QtWidgets.QLabel(self.birth)
        self.label_info_birth.setGeometry(QtCore.QRect(10,10,350,40))
        self.label_info_birth.setStyleSheet("color:black;\n")
        font=QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        self.label_info_birth.setFont(font)
        self.label_info_birth.setObjectName("label_info_birth")
        self.label_info_birth.setText("Birth Registration")
        ##############################################################################
        #############################################################################
        self.stackedWidget.addWidget(self.birth)
        self.death = QtWidgets.QWidget()
        self.death.setObjectName("death")
        self.label_info_death=QtWidgets.QLabel(self.death)
        self.label_info_death.setGeometry(QtCore.QRect(10,10,350,40))
        self.label_info_death.setStyleSheet("color:black;\n")
        font=QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        self.label_info_death.setFont(font)
        self.label_info_death.setObjectName("label_info_death")
        self.label_info_death.setText("Death Registration")
        ##############################################################################
        #############################################################################
        self.stackedWidget.addWidget(self.death)
        self.marriage = QtWidgets.QWidget()
        self.marriage.setObjectName("marriage")
        self.label_info_marriage=QtWidgets.QLabel(self.marriage)
        self.label_info_marriage.setGeometry(QtCore.QRect(10,10,350,40))
        self.label_info_marriage.setStyleSheet("color:black;\n")
        font=QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        self.label_info_marriage.setFont(font)
        self.label_info_marriage.setObjectName("label_info_marriage")
        self.label_info_marriage.setText("Marriage Registration")
        
        ##############################################################################
        #############################################################################
        self.stackedWidget.addWidget(self.marriage)
        self.divorce = QtWidgets.QWidget()
        self.divorce.setObjectName("divorce")
        self.label_info_divorce=QtWidgets.QLabel(self.divorce)
        self.label_info_divorce.setGeometry(QtCore.QRect(10,10,350,40))
        self.label_info_divorce.setStyleSheet("color:black;\n")
        font=QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        self.label_info_divorce.setFont(font)
        self.label_info_divorce.setObjectName("label_info_divorce")
        self.label_info_divorce.setText("Divorce Registration")
        ##############################################################################
        self.stackedWidget.addWidget(self.divorce)
        
        homeWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(homeWindow)
        self.statusbar.setObjectName("statusbar")
        homeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(homeWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(homeWindow)

    def retranslateUi(self, homeWindow):
        _translate = QtCore.QCoreApplication.translate
        homeWindow.setWindowTitle(_translate("homeWindow", "SMARTWARD"))
        self.pushButton_home.setText(_translate("homeWindow", "Home"))
        self.pushButton_birth.setText(_translate("homeWindow", "Birth"))
        self.pushButton_death.setText(_translate("homeWindow", "Death"))
        self.pushButton_marriage.setText(_translate("homeWindow", "Marriage"))
        self.pushButton_divorce.setText(_translate("homeWindow", "Divorce"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    homeWindow = QtWidgets.QMainWindow()
    ui = Ui_homeWindow()
    ui.setupUi(homeWindow)
    homeWindow.show()
    sys.exit(app.exec_())
