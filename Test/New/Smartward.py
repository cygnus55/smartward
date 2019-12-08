from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def refertohome(self):###refers to home page
        self.stackedWidget.setCurrentIndex(0)
        MainWindow.setWindowTitle("Smartward")
        
    def refertologin(self):###refers to login page
        self.stackedWidget.setCurrentIndex(2)
        MainWindow.setWindowTitle("Smartward-Login")
        
    def refertosignup(self):###refers to signup page
        self.stackedWidget.setCurrentIndex(1)
        MainWindow.setWindowTitle("Smartward-Signup")

    def exitwindow():
        Mainwindow.exit()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background:red;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(70, 30, 671, 491))
        self.stackedWidget.setStyleSheet("background:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stackedWidget.setObjectName("stackedWidget")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.loginpage_refer_fromhome = QtWidgets.QPushButton(self.home)
        self.loginpage_refer_fromhome.setGeometry(QtCore.QRect(390, 330, 211, 41))
        self.loginpage_refer_fromhome.setStyleSheet("color:white;\n"
"font-size:20px;")
        self.loginpage_refer_fromhome.setObjectName("loginpage_refer_fromhome")
        ##from home to login##################################################
        self.loginpage_refer_fromhome.clicked.connect(self.refertologin)
        ######################################################################
        self.signuppage_refer_fromhome = QtWidgets.QPushButton(self.home)
        self.signuppage_refer_fromhome.setGeometry(QtCore.QRect(390, 380, 211, 41))
        self.signuppage_refer_fromhome.setStyleSheet("color:white;\n"
"font-size:20px;")
        self.signuppage_refer_fromhome.setObjectName("signuppage_refer_fromhome")
         ##from home to signup##################################################
        self.signuppage_refer_fromhome.clicked.connect(self.refertosignup)
        ######################################################################
        self.homepage_info = QtWidgets.QLabel(self.home)
        self.homepage_info.setGeometry(QtCore.QRect(10, 70, 651, 171))
        self.homepage_info.setStyleSheet("color:white;\n"
"font-size:24px;\n"
"border-radius:20px;\n"                                        
"font-family:\"Consolas\";")
        self.homepage_info.setAlignment(QtCore.Qt.AlignCenter)
        self.homepage_info.setObjectName("homepage_info")
        self.exit_from_home = QtWidgets.QPushButton(self.home)
        self.exit_from_home.setGeometry(QtCore.QRect(390, 430, 211, 41))
        self.exit_from_home.setStyleSheet("color:white;\n"
"font-size:20px;")
        self.exit_from_home.setObjectName("exit_from_home")
        ####exit from home#############################################################
        self.exit_from_home.clicked.connect(self.exitwindow)
        #################################################################################
        self.stackedWidget.addWidget(self.home)
        self.signup = QtWidgets.QWidget()
        self.signup.setObjectName("signup")
        self.signup_groupbox = QtWidgets.QGroupBox(self.signup)
        self.signup_groupbox.setGeometry(QtCore.QRect(90, 40, 531, 361))
        self.signup_groupbox.setStyleSheet("background:rgb(0, 0, 255);")
        self.signup_groupbox.setTitle("")
        self.signup_groupbox.setAlignment(QtCore.Qt.AlignCenter)
        self.signup_groupbox.setObjectName("signup_groupbox")
        self.signup_label = QtWidgets.QLabel(self.signup_groupbox)
        self.signup_label.setGeometry(QtCore.QRect(220, 40, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.signup_label.setFont(font)
        self.signup_label.setStyleSheet("color:black;")
        self.signup_label.setAlignment(QtCore.Qt.AlignCenter)
        self.signup_label.setObjectName("signup_label")
        self.signup_fname_edit = QtWidgets.QLineEdit(self.signup_groupbox)
        self.signup_fname_edit.setGeometry(QtCore.QRect(40, 90, 221, 41))
        self.signup_fname_edit.setStyleSheet("border-radius:20px;\n"
"color:blue;\n"
"background:yellow;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"\n"
"")
        self.signup_fname_edit.setObjectName("signup_fname_edit")
        self.signup_lname_edit = QtWidgets.QLineEdit(self.signup_groupbox)
        self.signup_lname_edit.setGeometry(QtCore.QRect(280, 90, 221, 41))
        self.signup_lname_edit.setStyleSheet("border-radius:20px;\n"
"color:blue;\n"
"background:yellow;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"\n"
"")
        self.signup_lname_edit.setObjectName("signup_lname_edit")
        self.signup_username_edit = QtWidgets.QLineEdit(self.signup_groupbox)
        self.signup_username_edit.setGeometry(QtCore.QRect(40, 150, 221, 41))
        self.signup_username_edit.setStyleSheet("border-radius:20px;\n"
"color:blue;\n"
"background:yellow;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"\n"
"")
        self.signup_username_edit.setObjectName("signup_username_edit")
        self.signup_password_edit = QtWidgets.QLineEdit(self.signup_groupbox)
        self.signup_password_edit.setGeometry(QtCore.QRect(40, 210, 221, 41))
        self.signup_password_edit.setStyleSheet("border-radius:20px;\n"
"color:blue;\n"
"background:yellow;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"\n"
"")
        self.signup_password_edit.setObjectName("signup_password_edit")
        self.signup_year_edit = QtWidgets.QLineEdit(self.signup_groupbox)
        self.signup_year_edit.setGeometry(QtCore.QRect(50, 270, 81, 41))
        self.signup_year_edit.setStyleSheet("border-radius:20px;\n"
"color:blue;\n"
"background:yellow;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"\n"
"")
        self.signup_year_edit.setObjectName("signup_year_edit")
        self.signup_repassword_edit = QtWidgets.QLineEdit(self.signup_groupbox)
        self.signup_repassword_edit.setGeometry(QtCore.QRect(290, 210, 201, 41))
        self.signup_repassword_edit.setStyleSheet("border-radius:20px;\n"
"color:blue;\n"
"background:yellow;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"\n"
"")
        self.signup_repassword_edit.setObjectName("signup_repassword_edit")
        self.signup_month_edit = QtWidgets.QLineEdit(self.signup_groupbox)
        self.signup_month_edit.setGeometry(QtCore.QRect(150, 270, 81, 41))
        self.signup_month_edit.setStyleSheet("border-radius:20px;\n"
"color:blue;\n"
"background:yellow;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"\n"
"")
        self.signup_month_edit.setObjectName("signup_month_edit")
        self.signup_day_edit = QtWidgets.QLineEdit(self.signup_groupbox)
        self.signup_day_edit.setGeometry(QtCore.QRect(250, 270, 81, 41))
        self.signup_day_edit.setStyleSheet("border-radius:20px;\n"
"color:blue;\n"
"background:yellow;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"\n"
"")
        self.signup_day_edit.setObjectName("signup_day_edit")
        self.signup_pushbutton = QtWidgets.QPushButton(self.signup_groupbox)
        self.signup_pushbutton.setGeometry(QtCore.QRect(360, 310, 121, 41))
        self.signup_pushbutton.setStyleSheet("border-radius:20px;\n"
"color:black;\n"
"background:red;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"")
        self.signup_pushbutton.setObjectName("signup_pushbutton")        
        self.signin_refer_pushbutton = QtWidgets.QPushButton(self.signup)
        self.signin_refer_pushbutton.setGeometry(QtCore.QRect(230, 412, 261, 41))
        self.signin_refer_pushbutton.setStyleSheet("border-radius:20px;\n"
"color:black;\n"
"background:red;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"")
        self.signin_refer_pushbutton.setObjectName("signin_refer_pushbutton")
        ##refer to signin from signup##########################################
        self.signin_refer_pushbutton.clicked.connect(self.refertologin)
        ########################################################################
        self.home_from_signup = QtWidgets.QPushButton(self.signup)
        self.home_from_signup.setGeometry(QtCore.QRect(0, 0, 101, 41))
        self.home_from_signup.setStyleSheet("border-radius:20px;\n"
"color:black;\n"
"background:red;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"")
        self.home_from_signup.setObjectName("home_from_signup")
        ##from signup to home#########################################################
        self.home_from_signup.clicked.connect(self.refertohome)
        ##############################################################################
        self.exit_from_signuppage = QtWidgets.QPushButton(self.signup)
        self.exit_from_signuppage.setGeometry(QtCore.QRect(520, 412, 101, 41))
        self.exit_from_signuppage.setStyleSheet("border-radius:20px;\n"
"color:black;\n"
"background:red;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"")
        self.exit_from_signuppage.setObjectName("exit_from_signuppage")
        ####exit from signup#############################################################
        self.exit_from_signuppage.clicked.connect(self.exitwindow)
        #################################################################################
        self.stackedWidget.addWidget(self.signup)
        self.login = QtWidgets.QWidget()
        self.login.setObjectName("login")
        self.signin_groupbox = QtWidgets.QGroupBox(self.login)
        self.signin_groupbox.setGeometry(QtCore.QRect(70, 90, 531, 281))
        self.signin_groupbox.setStyleSheet("background:blue;")
        self.signin_groupbox.setTitle("")
        self.signin_groupbox.setObjectName("signin_groupbox")
        self.username_edit = QtWidgets.QLineEdit(self.signin_groupbox)
        self.username_edit.setGeometry(QtCore.QRect(160, 100, 221, 51))
        self.username_edit.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.username_edit.setStyleSheet("border-radius:20px;\n"
"color:blue;\n"
"background:yellow;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"\n"
"")
        self.username_edit.setText("")
        self.username_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.username_edit.setObjectName("username_edit")
        self.password_edit = QtWidgets.QLineEdit(self.signin_groupbox)
        self.password_edit.setGeometry(QtCore.QRect(160, 160, 221, 51))
        self.password_edit.setStyleSheet("border-radius:20px;\n"
"color:blue;\n"
"background:yellow;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"\n"
"\n"
"")
        self.password_edit.setText("")
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.password_edit.setObjectName("password_edit")
        self.signin_pushbutton = QtWidgets.QPushButton(self.signin_groupbox)
        self.signin_pushbutton.setGeometry(QtCore.QRect(200, 220, 151, 41))
        self.signin_pushbutton.setStyleSheet("border-radius:20px;\n"
"color:black;\n"
"background:red;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"\n"
"")
        self.signin_pushbutton.setObjectName("signin_pushbutton")
        self.signin_label = QtWidgets.QLabel(self.signin_groupbox)
        self.signin_label.setGeometry(QtCore.QRect(220, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.signin_label.setFont(font)
        self.signin_label.setStyleSheet("color:Black;\n"
"font-style:bold;\n"
"font-family:\"Consolas\";")
        self.signin_label.setAlignment(QtCore.Qt.AlignCenter)
        self.signin_label.setObjectName("signin_label")
        self.signin_password_label = QtWidgets.QLabel(self.signin_groupbox)
        self.signin_password_label.setGeometry(QtCore.QRect(46, 172, 101, 21))
        self.signin_password_label.setStyleSheet("font-size:18px;\n"
"font-family:\"arial\";")
        self.signin_password_label.setObjectName("signin_password_label")
        self.signin_username_label = QtWidgets.QLabel(self.signin_groupbox)
        self.signin_username_label.setGeometry(QtCore.QRect(46, 112, 101, 21))
        self.signin_username_label.setStyleSheet("font-size:18px;\n"
"font-family:\"arial\";")
        self.signin_username_label.setObjectName("signin_username_label")
        self.signup_refer_pushbutton = QtWidgets.QPushButton(self.login)
        self.signup_refer_pushbutton.setGeometry(QtCore.QRect(80, 390, 451, 41))
        self.signup_refer_pushbutton.setStyleSheet("border-radius:20px;\n"
"color:black;\n"
"background:red;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"")
        self.signup_refer_pushbutton.setObjectName("signup_refer_pushbutton")
        ##refer to signup from signin##########################################
        self.signup_refer_pushbutton.clicked.connect(self.refertosignup)
        ########################################################################
        self.home_from_signin = QtWidgets.QPushButton(self.login)
        self.home_from_signin.setGeometry(QtCore.QRect(0, 0, 101, 41))
        self.home_from_signin.setStyleSheet("border-radius:20px;\n"
"color:black;\n"
"background:red;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"")
        self.home_from_signin.setObjectName("home_from_signin")
        ##from signup to home##############################################
        self.home_from_signin.clicked.connect(self.refertohome)
        ###################################################################
        self.exit_from_signinpage = QtWidgets.QPushButton(self.login)
        self.exit_from_signinpage.setGeometry(QtCore.QRect(540, 390, 101, 41))
        self.exit_from_signinpage.setStyleSheet("border-radius:20px;\n"
"color:black;\n"
"background:red;\n"
"font-family:Consolas;\n"
"font-size:20px;\n"
"font-style:normal;\n"
"")
        self.exit_from_signinpage.setObjectName("exit_from_signinpage")
        ####exit from signin#############################################################
        self.exit_from_signinpage.clicked.connect(self.exitwindow)
        #################################################################################
        self.stackedWidget.addWidget(self.login)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Smartward"))
        self.loginpage_refer_fromhome.setText(_translate("MainWindow", "Login"))
        self.signuppage_refer_fromhome.setText(_translate("MainWindow", "Signup"))
        self.homepage_info.setText(_translate("MainWindow", " Welcome to our official software of Smartward!!!"))
        self.exit_from_home.setText(_translate("MainWindow", "Exit"))
        self.signup_label.setText(_translate("MainWindow", "Sign Up"))
        self.signup_fname_edit.setText(_translate("MainWindow", "First Name"))
        self.signup_lname_edit.setText(_translate("MainWindow", "Last Name"))
        self.signup_username_edit.setText(_translate("MainWindow", "Username"))
        self.signup_password_edit.setText(_translate("MainWindow", "Password"))
        self.signup_year_edit.setText(_translate("MainWindow", "Year"))
        self.signup_repassword_edit.setText(_translate("MainWindow", "Re-password"))
        self.signup_month_edit.setText(_translate("MainWindow", "Month"))
        self.signup_day_edit.setText(_translate("MainWindow", "Day"))
        self.signup_pushbutton.setText(_translate("MainWindow", "Sign up"))
        self.signin_refer_pushbutton.setText(_translate("MainWindow", "Or Sign in instead??"))
        self.home_from_signup.setText(_translate("MainWindow", "Home"))
        self.exit_from_signuppage.setText(_translate("MainWindow", "Exit"))
        self.signin_pushbutton.setText(_translate("MainWindow", "Sign in"))
        self.signin_label.setText(_translate("MainWindow", "Sign In"))
        self.signin_password_label.setText(_translate("MainWindow", "Password"))
        self.signin_username_label.setText(_translate("MainWindow", "Username"))
        self.signup_refer_pushbutton.setText(_translate("MainWindow", "Don\'t have an account!! Sign up instead!"))
        self.home_from_signin.setText(_translate("MainWindow", "Home"))
        self.exit_from_signinpage.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
