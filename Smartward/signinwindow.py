import re
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui_signinwindow import *

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	#Application start to run
	MainWindow.show()
    
	#definition of signinwindow functions
	def on_signup_clicked():
		print("signin clicked")
		"""
		-get values from line edits
		--check if all fields are filled(except logo)
		---connect to database
		----check municipality and ward no.(if resemble to any other values)
		-----check email (if resemble)
		------get system ip address
		-------store to ward_info table
		--------create new table for that ward
		---------send mail to client to give id and other info
		"""
	def on_signin_2_clicked():
		#go to signinPage
		ui.signStack.setCurrentIndex(1)
		
	def on_signin_clicked():
		print("signin clicked")
		"""
		-get id or email and password from line edits
		--connect to database
		---check email or id to resemble
		----check password
		----if new ip address replace in table
		-----send mail to inform sign in
		-----go to smart ward main workstation
		"""
		
	def on_signup_2_clicked():
		#go to signupPage
		ui.signStack.setCurrentIndex(0)
		
	def on_forgetPassword_clicked():
		print("forget password")
		#left to work on
		#not created any page for this function
    
	#set to sign up page
	ui.signStack.setCurrentIndex(0)
     
	#sign up page functions
	ui.signup.setAutoDefault(True)
	ui.signup.clicked.connect(on_signup_clicked)
	ui.signin_2.setAutoDefault(True)
	ui.signin_2.clicked.connect(on_signin_2_clicked)
    
	#sign in page functions
	ui.signin.setAutoDefault(True)
	ui.signin.clicked.connect(on_signin_clicked)
	ui.signup_2.setAutoDefault(True)
	ui.signup_2.clicked.connect(on_signup_2_clicked)
	ui.forgetPassword.setAutoDefault(True)
	ui.forgetPassword.clicked.connect(on_forgetPassword_clicked)
    
	sys.exit(app.exec_())
