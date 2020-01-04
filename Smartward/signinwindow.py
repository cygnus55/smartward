import re
import socket
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from ui_signinwindow import *
from sw_string import *
from dbconnect import *
from swgmail import *

db=database_signinwindow("localhost","root","smartward")
mygmail=SWGmail()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.mun_logo.setEchoMode(0)
    # Application start to run
    MainWindow.show()


    # definition of signinwindow functions
    def on_signup_clicked():
        print("signup clicked")
        #get valuse from line edits
        municipality=ui.municipality.text().title()
        wardno=ui.wardno.text()
        address=ui.address.text().title()
        state=ui.state.text()
        phone=ui.phoneNo.text()
        email=ui.email.text()
        mun_logo=ui.mun_logo.text()
        password=ui.password.text()
        confirmpassword = ui.confirmpassword.text()

        #check if all fields are filled
        if(isEmpty(municipality,wardno,address,phone,email,password,confirmpassword)):
            QMessageBox.warning(ui,"SignUp Failed","All fields are not filled!")
        elif(not(password == confirmpassword)):
            QMessageBox.warning(ui,"Password Confirmation Invalid","Password doesnot match!")
        else:
            db.createWardTable()
            if(not db.checkValid(municipality,wardno)):
                QMessageBox.information(ui,"SignUp Failed","Ward Office already Registered!")
            else:
                if(not db.checkEmailValid(email)):
                    QMessageBox.information(ui,"Signup Failed","Email Already in Use.Try another email.")
                else:
                    id=generateID(municipality.lower(),wardno,state)
                    print(id)
                    ip = socket.gethostbyname(socket.gethostname())
                    if(db.InsertIntoward_registrationTable(id,municipality,wardno,state,address,phone,email,"****",mun_logo,password)):
                        mygmail.sendRegistrationSuccessfulMail(id,municipality,wardno,state,address,phone,email,ip,password)
                        QMessageBox.information(ui,"Registration Sucessful","We have sent mail to your email account.\nCheck the mail for login details.")

    def on_browse_clicked():
        print("browse clicked")
        #set browse file for images
        path=QFileDialog.getOpenFileName(ui,"Municipality Logo","/home","Images(*.png)")[0]
        ui.mun_logo.setText(path)

    def on_signin_2_clicked():
        # go to signinPage
        ui.signStack.setCurrentIndex(2)


    def on_signin_clicked():
        #get id or email and password from line edits
        login_id=ui.login_id.text()
        login_password=ui.login_password.text()
        if (isEmpty(login_id,login_password)):
            QMessageBox.warning(ui,"Login Unsucessful","Login ID or Password is Missing!")
        else:
            ip,email,id=db.checkLoginValidity(login_id,login_password)
            print(ip,email,id)
            if(ip=="invalid" and email=="" and id==""):
                QMessageBox.warning(ui,"Login Unsucessful","Login ID or Password Invalid")
            else:
                ip_add = socket.gethostbyname(socket.gethostname())
                if not(ip==ip_add):
                    db.updateIP(login_id,ip_add)
                mygmail.sendLoginMail(email,ip)
                #goto smartward main window


            """
            get id or email and password from line edits
            --connect to database
            ---check email or id to resemble
            ----check password
            ----if new ip address replace in table
            -----send mail to inform sign in
            -----go to smart ward main workstation
            """


    def on_signup_2_clicked():
        # go to signupPage
        ui.signStack.setCurrentIndex(0)


    def on_forgetPassword_clicked():
        # go to forget password page
        ui.signStack.setCurrentIndex(1)


    def on_sendEmail_clicked():
        print("send email clicked")
        gmail=ui.login_id_2.text()
        login_details = db.checkEmailValidity(gmail)
        if not(login_details):
            QMessageBox.warning(ui,"Forget Password","Invalid Email Id")
        else:
            id,email,pswd=login_details[0][0],login_details[0][6],login_details[0][-1]
            mygmail.sendForgetPasswordMail(id,email,pswd)
            QMessageBox.information(ui,"Forget Password","Email has been sent to you\nwith your login details")
        """
        -connect to database
        --check if that email exists
        ---import gmail module
        ----send email to required ward
        """


    # set to sign up page
    ui.signStack.setCurrentIndex(0)

    # sign up page functions
    ui.signup.setAutoDefault(True)
    ui.signup.clicked.connect(on_signup_clicked)
    ui.browse.setAutoDefault(True)
    ui.browse.clicked.connect(on_browse_clicked)
    ui.signin_2.setAutoDefault(True)
    ui.signin_2.clicked.connect(on_signin_2_clicked)

    # sign in page functions
    ui.signin.setAutoDefault(True)
    ui.signin.clicked.connect(on_signin_clicked)
    ui.signup_2.setAutoDefault(True)
    ui.signup_2.clicked.connect(on_signup_2_clicked)
    ui.forgetPassword.setAutoDefault(True)
    ui.forgetPassword.clicked.connect(on_forgetPassword_clicked)

    # forget password functions
    ui.signin_3.setAutoDefault(True)
    ui.signin_3.clicked.connect(on_signin_2_clicked)
    ui.sendEmail.setAutoDefault(True)
    ui.sendEmail.clicked.connect(on_sendEmail_clicked)

    sys.exit(app.exec_())
