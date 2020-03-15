#Copy this in every code:
#self.window_functions(WardWindow)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import pickle
import sys
import os
import time

from sw_string import isEmpty,generateID,generateList
from sw_gmail import *
import dbconnect 
import graph
#importing registration forms
from forms import marriage
from forms import birth
from forms import death
from forms import divorce
from forms import migration
#importing citizenship related forms
from forms.sifaris import citizenshiprequest
from forms.sifaris import citizenshipcopy
#importing recommendation forms
from forms.sifaris import gharbato
from forms.sifaris import incomereco
from forms.sifaris import typerecommendation
#import receipt
from receipt import receipt

#myemail=SWGmail()

class Ui_WardWindow(QWidget):
    def window_functions(self,MainWindow):
        #set Logo in MainWindow
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("sw_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        def ward_load_data():
            #this loads the info from ward.pickle file
            try:
                with open('ward.pickle','rb') as obj:
                    read=pickle.load(obj)
                    mun_name,mun_ward_num,state_num,mun_logo=read['municipality'],read['wardno'],read['state'],read['mun_logo']
                    print(mun_name,mun_ward_num,state_num,mun_logo)
                    if not isEmpty(mun_logo):
                        mun_logo_pixmap=QtGui.QPixmap(mun_logo)
                        self.mun_logo_label.setPixmap(mun_logo_pixmap)
                        self.mun_logo_label.setScaledContents(True)
                    else:
                        self.mun_logo_label.setText("")
                    self.Mun_Name.setText("{} Municipality".format(mun_name))
                    self.Mun_Ward_num.setText(f"Ward No.: {mun_ward_num} , State : {state_num}")
            except FileNotFoundError:
                print("Ward not registered.")
        
        def check_registrar():
            try:
                with open('ward.pickle','rb') as f:
                    read=pickle.load(f)
                if (not isEmpty(read['registrar_name'],read['registrar_post'])):
                    return True
                else:
                    QMessageBox.warning(self,"No registrar","Enter the registrar details for operation.")
                    update_registrar_page() 
                    return False
            except Exception as e:
                print(e)


        def clear_lineedits():
            #clear_lineedits:
            #from update_profile_page
            self.municipality_update_lineedit.clear()
            self.ward_no_update_lineedit.clear()
            self.address_update_lineedit.clear()
            self.state_update_lineedit.clear()
            self.email_update_lineedit.clear()
            self.phone_update_lineedit.clear()
            self.logo_path_update_lineedit.clear()
            #from change_password_page
            self.old_password_lineedit.clear()
            self.new_password_linedit.clear()
            self.reconfirm_password_lineedit.clear()
            #from delete_ward_page
            self.deletion_password_lineedit.clear()
            #from update_registrar_page
            self.registrar_name_lineedit.clear()
            self.registrar_post_lineedit.clear()



        #on_home_button_clicked,remove_account,change_destination_folder help navigate between stackWidget pages
        def home_page():
            #home page
            print("home page")
            clear_lineedits()
            self.stackedWidget.setCurrentIndex(0)

        def update_ward_profile_page():
            #ward profile page
            print("ward profile page")
            clear_lineedits()
            self.stackedWidget.setCurrentIndex(3)

        def change_password_page():
            #change password page
            print("change password page")
            clear_lineedits()
            self.stackedWidget.setCurrentIndex(1)

        def remove_account_page():
            #remove account page
            print("remove account page")
            clear_lineedits()
            self.stackedWidget.setCurrentIndex(2)

        def update_registrar_page():
            #update registrar page
            print("update registrar page")
            clear_lineedits()
            self.stackedWidget.setCurrentIndex(4)

        #these are the ward functions
        def on_browse_clicked():
            print("browse clicked")
            path=QFileDialog.getOpenFileName(self,"Municipality Logo",sys.path[0]+"\Logo","Images(*.png)")[0]
            self.logo_path_update_lineedit.setText(path)

        def on_ward_profile_update_clicked():
            #ward profile update
            municipality=self.municipality_update_lineedit.text().title()
            wardno=self.ward_no_update_lineedit.text()
            address=self.address_update_lineedit.text().title()
            state=self.state_update_lineedit.text()
            email=self.email_update_lineedit.text()
            phone=self.phone_update_lineedit.text()
            mun_logo=self.logo_path_update_lineedit.text()
            ward={'municipality':municipality,'wardno':wardno,'state':state,'address':address,'phone':phone,'email':email,'mun_logo':mun_logo}
            with open("ward.pickle",'rb') as f:
                read=pickle.load(f)
            for key in ward:
                if not isEmpty(ward[key]):
                    read[key]=ward[key]
                    print("{} changed.".format(key))  
            print("Id changed: {}".format(read['id']))
            with open("ward.pickle",'wb') as f:
                    pickle.dump(read,f)
            ward_load_data()
            home_page()
            print(read)

        def on_change_password_clicked():
            #change password
            old_pwd=self.old_password_lineedit.text()
            new_pwd=self.new_password_linedit.text()
            re_new_pwd=self.reconfirm_password_lineedit.text()
            with open("ward.pickle",'rb') as f:
                read=pickle.load(f)
                data=read
                pwd=read['password']
            if isEmpty(old_pwd,new_pwd,re_new_pwd):
                QMessageBox.warning(self,"Empty Field","Please enter all the passwords!!!")
            elif not(old_pwd==pwd):
                self.old_password_lineedit.clear()
                QMessageBox.warning(self,"Wrong Password","Wrong old password.")
            elif not (new_pwd==re_new_pwd):
                self.new_password_linedit.clear()
                self.reconfirm_password_lineedit.clear()
                QMessageBox.warning(self,"Password Error","New passwords do not match.")
            else:
                data['password']=new_pwd
                with open("ward.pickle",'wb') as f:
                    pickle.dump(data,f)
                QMessageBox.information(self,"Password Changed","Password Changed Successfully.")
                home_page()


        def on_remove_account_clicked():
            #remove ward account
            pwd=self.deletion_password_lineedit.text()
            with open('ward.pickle','rb') as f:
                read=pickle.load(f)
                password=read['password']
            if (isEmpty(pwd)):
                clear_lineedits()
                QMessageBox.warning(self,"Empty field","Enter the password for deletion!!!")
            elif password==pwd:
                buttonReply = QMessageBox.question(self, 'Account deletion', "Once deleted, the account cannot be retreived.\n Are you sure you want to delete your account?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    print('Exiting window....')
                    MainWindow.setWindowTitle("SmartWard ---account deletion")
                    time.sleep(5)
                    MainWindow.close()
                    print('Window Exited.')
                    with open('ward.pickle','rb') as f:
                        read=pickle.load(f)
                        f.close()
                    read['registration_status']=False
                    with open('ward.pickle','wb') as f:
                        pickle.dump(read,f)
                        f.close()
                    sys.exit()
                else:
                    print('Account deletion aborted.')
                    home_page()
            else:
                QMessageBox.warning(self,"Wrong password","Enter the correct password for deletion!!!")
                clear_lineedits()

        def on_registrar_update_clicked():
            #update local registrar
            registrar_name=self.registrar_name_lineedit.text()
            registrar_post=self.registrar_post_lineedit.text()
            with open('ward.pickle','rb') as f:
                read=pickle.load(f)
            print(read)
            if not isEmpty(registrar_name,registrar_post):
                read['registrar_name']=registrar_name
                read['registrar_post']=registrar_post
                with open('ward.pickle','wb') as f:
                    pickle.dump(read,f)
                home_page()
            else:
                QMessageBox.warning(self,"Empty Field","Enter the complete details for updating!!!")

        def on_remove_registrar_clicked():
            with open('ward.pickle','rb') as fileobj:
                read=pickle.load(fileobj)
            print(read)
            if isEmpty(read['registrar_name']) and isEmpty(read['registrar_post']):
                QMessageBox.information(self,"Empty Local Registrar","Local Registrar Details not registered.")
            else:
                read['registrar_name']=''
                read['registrar_post']=''
                print(read)
                with open('ward.pickle','wb') as fileobj:
                    pickle.dump(read,fileobj)
                home_page()
                QMessageBox.information(self,"Remove Local Registrar","Local registrar details successfully removed.")
                

        #open respective forms
        def birth_reg():
            #birth registration
            #new Window-birth reg. form 
            if (check_registrar()):
                self.birth_form=birth.ActualWork()
                print("birth registration")
            
        
        def death_reg():
            #death registration
            #new Window-death reg. form
            if (check_registrar()):
                self.death_form=death.ActualWork()
                print("death registration")
            
        def marriage_reg():
            #marriage registration
            #new Window-marriage reg. form
            if (check_registrar()):
                self.marriage_form=marriage.ActualWork()
                print("marriage registration")

        def divorce_reg():
            #divorce registration
            #new Window-divorce reg. form
            if (check_registrar()):
                self.death_form=divorce.ActualWork()
                print("divorce registration") 
                
        def migration_reg():
            #migration registration
            #new Window-migration reg. form
            if (check_registrar()):
                self.migration_form=migration.ActualWork()
                print("migration registration")
        
        def citizenship_request():
            if (check_registrar()):
                cit_req=citizenshiprequest.ActualWork()
                print("citizenship request form")

        def citizenship_copy():
            if (check_registrar()):
                cit_copy=citizenshipcopy.ActualWork()
                print("citizenship copy form")

        def gharbato_reco():
            if (check_registrar()):
                gharbato_form=gharbato.ActualWork()
                print("gharbaato recommendation form")
        
        def income_reco():
            if (check_registrar()):
                income_reco_form=incomereco.ActualWork()
                print("income recommendation form")
        
        def type_recommendation():
            if (check_registrar()):
                #type_reco_form=typerecommendation.ActualWork()
                self.typerecowindow = QtWidgets.QMainWindow()
                self.ui = typerecommendation.Ui_TypeReco()
                self.ui.setupUi(self.typerecowindow)
                self.typerecowindow.show()
                print("type recommendation form")

        def on_receipt_clicked():
            if (check_registrar()):
                receipt.ActualWork()

        def statistics_show(name,table_name):
            #self.stat_window=graph.StatWindow()
            #self.start_window.show()
            StatWindow=QtWidgets.QMainWindow()
            window = graph.Ui_StatWindow(name,table_name)
            window.setupUi(StatWindow)
            StatWindow.show()
            print(f"StatWindow displayed: {name} and {table_name} table.")
        

        self.home_button.clicked.connect(home_page)
        self.delete_account_button.clicked.connect(on_remove_account_clicked)
        self.change_password_button.clicked.connect(on_change_password_clicked)
        self.update_ward_profile_button.clicked.connect(on_ward_profile_update_clicked)
        self.browse.clicked.connect(on_browse_clicked)
        self.update_registrar_button.clicked.connect(on_registrar_update_clicked)
        self.remove_registrar_button.clicked.connect(on_remove_registrar_clicked)
        self.receipt_button.clicked.connect(on_receipt_clicked)
        sifaris_menu=QtWidgets.QMenu()
        sifaris_menu.addAction("Gharbato Recommendation Form",gharbato_reco)
        sifaris_menu.addAction("Income Source Recommendation Form",income_reco)
        sifaris_menu.addAction("Type recommendation Form",type_recommendation)
        self.sifarish_button.setMenu(sifaris_menu)
        
        citizenship_menu=QtWidgets.QMenu()
        citizenship_menu.addAction("Citizenship request",citizenship_request)
        citizenship_menu.addAction("Request Copy of Citizenship",citizenship_copy)
        self.citizenship_button.setMenu(citizenship_menu)
        
        
        statistics_menu=QtWidgets.QMenu()
        statistics_menu.addAction("View Birth Statistics",lambda:statistics_show('Birth','BirthRegistration'))
        statistics_menu.addAction("View Death Statistics",lambda:statistics_show('Death','DeathRegistration'))
        statistics_menu.addAction("View Marriage Statistics",lambda:statistics_show('Marriage','MarriageRegistration'))
        statistics_menu.addAction("View Divorce Statistics",lambda:statistics_show('Divorce','DivorceRegistration'))
        statistics_menu.addAction("View Migration Statistics",lambda:statistics_show('Migration','MigrationRegistration'))
        statistics_menu.addAction("View Receipt Statistics",citizenship_copy)
        self.statistics_button.setMenu(statistics_menu)
        

        settings_menu=QtWidgets.QMenu()
        settings_menu.addAction("Update Ward Profile",update_ward_profile_page)
        settings_menu.addAction("Change Password",change_password_page)
        settings_menu.addAction("Remove Ward Account",remove_account_page)
        settings_menu.addAction("Update Registrar Details",update_registrar_page)
        self.settings_button.setMenu(settings_menu)
        
        vital_reg_menu=QtWidgets.QMenu()
        vital_reg_menu.addAction("Birth registration",birth_reg)
        vital_reg_menu.addAction("Death registration",death_reg)
        vital_reg_menu.addAction("Marriage registration",marriage_reg)
        vital_reg_menu.addAction("Divorce registration",divorce_reg)
        vital_reg_menu.addAction("Migration registration",migration_reg)
        self.vital_reg_button.setMenu(vital_reg_menu)

        ward_load_data()

    def setupUi(self, WardWindow):
        WardWindow.setObjectName("WardWindow")
        WardWindow.resize(1366, 768)
        WardWindow.setMinimumSize(QtCore.QSize(1366, 768))
        WardWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget = QtWidgets.QWidget(WardWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1346, 748))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1902, 200))
        self.frame.setStyleSheet("QFrame\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgb(248, 244, 255);\n"
"}\n"
"QPushButton\n"
"{\n"
"font-size:16px;\n"
"}\n"
"QLabel\n"
"{\n"
"color:red;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.nepal_gov_logo = QtWidgets.QLabel(self.frame)
        self.nepal_gov_logo.setGeometry(QtCore.QRect(0, 10, 150, 148))
        self.nepal_gov_logo.setStyleSheet("border-image: url(:/pic/logo.png);")
        self.nepal_gov_logo.setText("")
        self.nepal_gov_logo.setObjectName("nepal_gov_logo")
        self.Mun_Name = QtWidgets.QLabel(self.frame)
        self.Mun_Name.setGeometry(QtCore.QRect(185, 30, 616, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Mun_Name.setFont(font)
        self.Mun_Name.setStyleSheet("")
        self.Mun_Name.setText("")
        self.Mun_Name.setObjectName("Mun_Name")
        self.home_button = QtWidgets.QPushButton(self.frame)
        self.home_button.setGeometry(QtCore.QRect(10, 163, 121, 30))
        self.home_button.setStyleSheet("border-radius:6px;\n"
"border:1px solid rgb(170, 170, 127);\n"
"qproperty-icon:url(:pic/home-icon.png);\n"
"")
        self.home_button.setObjectName("home_button")
        self.settings_button = QtWidgets.QPushButton(self.frame)
        self.settings_button.setGeometry(QtCore.QRect(135, 163, 136, 30))
        self.settings_button.setStyleSheet("border-radius:6px;\n"
"border:1px solid rgb(170, 170, 127);\n"
"qproperty-icon:url(:pic/settings-icon.png);")
        self.settings_button.setObjectName("settings_button")
        self.mun_logo_label = QtWidgets.QLabel(self.frame)
        self.mun_logo_label.setGeometry(QtCore.QRect(1170, 10, 150, 148))
        self.mun_logo_label.setText("")
        self.mun_logo_label.setObjectName("mun_logo_label")
        self.Mun_Ward_num = QtWidgets.QLabel(self.frame)
        self.Mun_Ward_num.setGeometry(QtCore.QRect(185, 60, 600, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Mun_Ward_num.setFont(font)
        self.Mun_Ward_num.setStyleSheet("")
        self.Mun_Ward_num.setText("")
        self.Mun_Ward_num.setObjectName("Mun_Ward_num")
        self.stackedWidget = QtWidgets.QStackedWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 200, 1366, 568))
        self.stackedWidget.setStyleSheet("QPushButton:hover\n"
"{\n"
"background-color:rgb(248, 244, 255);\n"
"}\n"
"QPushButton#delete_account_button:hover{\n"
"background-color:rgb(255, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton#change_password_button:hover{\n"
"background-color: rgb(170, 170, 255);\n"
"color:rgb(0, 0, 127);\n"
"}\n"
"QPushButton#delete_account_button\n"
"{\n"
"background-color:rgb(248, 244, 255);\n"
"}\n"
"QPushButton#change_password_button\n"
"{\n"
"background-color:rgb(248, 244, 255);\n"
"}\n"
"QPushButton{\n"
"border-radius:10px;\n"
"border:1px solid rgb(170, 170, 127);\n"
"font-size:16px;\n"
"}\n"
"QWidget\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.home_page = QtWidgets.QWidget()
        self.home_page.setObjectName("home_page")
        self.vital_reg_button = QtWidgets.QPushButton(self.home_page)
        self.vital_reg_button.setGeometry(QtCore.QRect(30, 75, 540, 91))
        self.vital_reg_button.setStyleSheet("")
        self.vital_reg_button.setObjectName("vital_reg_button")
        self.citizenship_button = QtWidgets.QPushButton(self.home_page)
        self.citizenship_button.setGeometry(QtCore.QRect(30, 220, 540, 91))
        self.citizenship_button.setObjectName("citizenship_button")
        self.sifarish_button = QtWidgets.QPushButton(self.home_page)
        self.sifarish_button.setGeometry(QtCore.QRect(690, 75, 540, 91))
        self.sifarish_button.setObjectName("sifarish_button")
        self.receipt_button = QtWidgets.QPushButton(self.home_page)
        self.receipt_button.setGeometry(QtCore.QRect(690, 220, 540, 91))
        self.receipt_button.setObjectName("receipt_button")
        self.statistics_button = QtWidgets.QPushButton(self.home_page)
        self.statistics_button.setGeometry(QtCore.QRect(30, 375, 540, 91))
        self.statistics_button.setObjectName("statistics_button")
        self.stackedWidget.addWidget(self.home_page)
        self.change_password = QtWidgets.QWidget()
        self.change_password.setObjectName("change_password")
        self.groupBox = QtWidgets.QGroupBox(self.change_password)
        self.groupBox.setGeometry(QtCore.QRect(180, 90, 496, 256))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.old_password_lineedit = QtWidgets.QLineEdit(self.groupBox)
        self.old_password_lineedit.setGeometry(QtCore.QRect(75, 45, 256, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.old_password_lineedit.setFont(font)
        self.old_password_lineedit.setStyleSheet("border-radius:6px;\n"
"border:1px solid rgb(170, 170, 127);")
        self.old_password_lineedit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.old_password_lineedit.setObjectName("old_password_lineedit")
        self.new_password_linedit = QtWidgets.QLineEdit(self.groupBox)
        self.new_password_linedit.setGeometry(QtCore.QRect(75, 90, 256, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.new_password_linedit.setFont(font)
        self.new_password_linedit.setStyleSheet("border-radius:6px;\n"
"border:1px solid rgb(170, 170, 127);")
        self.new_password_linedit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_password_linedit.setObjectName("new_password_linedit")
        self.reconfirm_password_lineedit = QtWidgets.QLineEdit(self.groupBox)
        self.reconfirm_password_lineedit.setGeometry(QtCore.QRect(75, 135, 256, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reconfirm_password_lineedit.setFont(font)
        self.reconfirm_password_lineedit.setStyleSheet("border-radius:6px;\n"
"border:1px solid rgb(170, 170, 127);")
        self.reconfirm_password_lineedit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.reconfirm_password_lineedit.setObjectName("reconfirm_password_lineedit")
        self.change_password_button = QtWidgets.QPushButton(self.groupBox)
        self.change_password_button.setGeometry(QtCore.QRect(300, 195, 151, 31))
        self.change_password_button.setObjectName("change_password_button")
        self.stackedWidget.addWidget(self.change_password)
        self.remove_ward_page = QtWidgets.QWidget()
        self.remove_ward_page.setObjectName("remove_ward_page")
        self.groupBox_2 = QtWidgets.QGroupBox(self.remove_ward_page)
        self.groupBox_2.setGeometry(QtCore.QRect(180, 90, 481, 211))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(15, 30, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.deletion_password_lineedit = QtWidgets.QLineEdit(self.groupBox_2)
        self.deletion_password_lineedit.setGeometry(QtCore.QRect(30, 90, 256, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.deletion_password_lineedit.setFont(font)
        self.deletion_password_lineedit.setStyleSheet("border: 1px solid rgb(170, 170, 127);\n"
"border-radius:6px;\n"
"")
        self.deletion_password_lineedit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.deletion_password_lineedit.setObjectName("deletion_password_lineedit")
        self.delete_account_button = QtWidgets.QPushButton(self.groupBox_2)
        self.delete_account_button.setGeometry(QtCore.QRect(240, 150, 136, 31))
        self.delete_account_button.setObjectName("delete_account_button")
        self.stackedWidget.addWidget(self.remove_ward_page)
        self.update_ward_profile_page = QtWidgets.QWidget()
        self.update_ward_profile_page.setObjectName("update_ward_profile_page")
        self.groupBox_3 = QtWidgets.QGroupBox(self.update_ward_profile_page)
        self.groupBox_3.setGeometry(QtCore.QRect(105, 45, 721, 421))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("QLineEdit\n"
"{\n"
"    border: 1px solid rgb(170, 170, 127);\n"
"    border-radius:6px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"color:rgb(0, 0, 127);\n"
"}")
        self.groupBox_3.setObjectName("groupBox_3")
        self.municipality_update_lineedit = QtWidgets.QLineEdit(self.groupBox_3)
        self.municipality_update_lineedit.setGeometry(QtCore.QRect(105, 75, 286, 31))
        self.municipality_update_lineedit.setStyleSheet("")
        self.municipality_update_lineedit.setObjectName("municipality_update_lineedit")
        self.address_update_lineedit = QtWidgets.QLineEdit(self.groupBox_3)
        self.address_update_lineedit.setGeometry(QtCore.QRect(105, 120, 286, 31))
        self.address_update_lineedit.setStyleSheet("")
        self.address_update_lineedit.setObjectName("address_update_lineedit")
        self.email_update_lineedit = QtWidgets.QLineEdit(self.groupBox_3)
        self.email_update_lineedit.setGeometry(QtCore.QRect(105, 165, 286, 31))
        self.email_update_lineedit.setObjectName("email_update_lineedit")
        self.phone_update_lineedit = QtWidgets.QLineEdit(self.groupBox_3)
        self.phone_update_lineedit.setGeometry(QtCore.QRect(105, 210, 286, 31))
        self.phone_update_lineedit.setObjectName("phone_update_lineedit")
        self.logo_path_update_lineedit = QtWidgets.QLineEdit(self.groupBox_3)
        self.logo_path_update_lineedit.setGeometry(QtCore.QRect(105, 255, 286, 31))
        self.logo_path_update_lineedit.setObjectName("logo_path_update_lineedit")
        self.state_update_lineedit = QtWidgets.QLineEdit(self.groupBox_3)
        self.state_update_lineedit.setGeometry(QtCore.QRect(435, 120, 151, 31))
        self.state_update_lineedit.setObjectName("state_update_lineedit")
        self.ward_no_update_lineedit = QtWidgets.QLineEdit(self.groupBox_3)
        self.ward_no_update_lineedit.setGeometry(QtCore.QRect(435, 75, 151, 31))
        self.ward_no_update_lineedit.setObjectName("ward_no_update_lineedit")
        self.browse = QtWidgets.QPushButton(self.groupBox_3)
        self.browse.setGeometry(QtCore.QRect(420, 255, 41, 31))
        self.browse.setStyleSheet("border: 2px solid black;\n"
"border-radius:0px;\n"
"border-image:url(:/pic/browse.png);\n"
"\n"
"")
        self.browse.setText("")
        self.browse.setObjectName("browse")
        self.update_ward_profile_button = QtWidgets.QPushButton(self.groupBox_3)
        self.update_ward_profile_button.setGeometry(QtCore.QRect(375, 330, 166, 31))
        self.update_ward_profile_button.setObjectName("update_ward_profile_button")
        self.stackedWidget.addWidget(self.update_ward_profile_page)
        self.update_registrar_details_page = QtWidgets.QWidget()
        self.update_registrar_details_page.setObjectName("update_registrar_details_page")
        self.groupBox_4 = QtWidgets.QGroupBox(self.update_registrar_details_page)
        self.groupBox_4.setGeometry(QtCore.QRect(195, 75, 481, 241))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet("QLineEdit\n"
"{\n"
"border-radius:6px;\n"
"border: 1px solid rgb(170, 170, 127); \n"
"padding:5px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"color:rgb(0, 0, 127);\n"
"}")
        self.groupBox_4.setObjectName("groupBox_4")
        self.update_registrar_button = QtWidgets.QPushButton(self.groupBox_4)
        self.update_registrar_button.setGeometry(QtCore.QRect(315, 180, 136, 31))
        self.update_registrar_button.setObjectName("update_registrar_button")
        self.registrar_name_lineedit = QtWidgets.QLineEdit(self.groupBox_4)
        self.registrar_name_lineedit.setGeometry(QtCore.QRect(30, 60, 316, 31))
        self.registrar_name_lineedit.setText("")
        self.registrar_name_lineedit.setObjectName("registrar_name_lineedit")
        self.registrar_post_lineedit = QtWidgets.QLineEdit(self.groupBox_4)
        self.registrar_post_lineedit.setGeometry(QtCore.QRect(30, 120, 316, 31))
        self.registrar_post_lineedit.setObjectName("registrar_post_lineedit")
        self.remove_registrar_button = QtWidgets.QPushButton(self.groupBox_4)
        self.remove_registrar_button.setGeometry(QtCore.QRect(165, 180, 136, 31))
        self.remove_registrar_button.setObjectName("remove_registrar_button")
        self.stackedWidget.addWidget(self.update_registrar_details_page)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        WardWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(WardWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.window_functions(WardWindow)
        QtCore.QMetaObject.connectSlotsByName(WardWindow)
        WardWindow.setTabOrder(self.scrollArea, self.home_button)
        WardWindow.setTabOrder(self.home_button, self.settings_button)
        WardWindow.setTabOrder(self.settings_button, self.vital_reg_button)
        WardWindow.setTabOrder(self.vital_reg_button, self.sifarish_button)
        WardWindow.setTabOrder(self.sifarish_button, self.citizenship_button)
        WardWindow.setTabOrder(self.citizenship_button, self.receipt_button)
        WardWindow.setTabOrder(self.receipt_button, self.old_password_lineedit)
        WardWindow.setTabOrder(self.old_password_lineedit, self.new_password_linedit)
        WardWindow.setTabOrder(self.new_password_linedit, self.reconfirm_password_lineedit)
        WardWindow.setTabOrder(self.reconfirm_password_lineedit, self.change_password_button)
        WardWindow.setTabOrder(self.change_password_button, self.deletion_password_lineedit)
        WardWindow.setTabOrder(self.deletion_password_lineedit, self.delete_account_button)
        WardWindow.setTabOrder(self.delete_account_button, self.municipality_update_lineedit)
        WardWindow.setTabOrder(self.municipality_update_lineedit, self.ward_no_update_lineedit)
        WardWindow.setTabOrder(self.ward_no_update_lineedit, self.address_update_lineedit)
        WardWindow.setTabOrder(self.address_update_lineedit, self.state_update_lineedit)
        WardWindow.setTabOrder(self.state_update_lineedit, self.email_update_lineedit)
        WardWindow.setTabOrder(self.email_update_lineedit, self.phone_update_lineedit)
        WardWindow.setTabOrder(self.phone_update_lineedit, self.logo_path_update_lineedit)
        WardWindow.setTabOrder(self.logo_path_update_lineedit, self.browse)
        WardWindow.setTabOrder(self.browse, self.update_ward_profile_button)

    def retranslateUi(self, WardWindow):
        _translate = QtCore.QCoreApplication.translate
        WardWindow.setWindowTitle(_translate("WardWindow", "SmartWard"))
        self.home_button.setText(_translate("WardWindow", "Home"))
        self.settings_button.setText(_translate("WardWindow", "Settings"))
        self.vital_reg_button.setText(_translate("WardWindow", "Vital Registration"))
        self.citizenship_button.setText(_translate("WardWindow", "Citizenship"))
        self.sifarish_button.setText(_translate("WardWindow", "Sifaris (Recommendation Forms)"))
        self.receipt_button.setText(_translate("WardWindow", "Receipt"))
        self.statistics_button.setText(_translate("WardWindow", "Statistics"))
        self.groupBox.setTitle(_translate("WardWindow", "Change Password:"))
        self.old_password_lineedit.setPlaceholderText(_translate("WardWindow", " Current Password"))
        self.new_password_linedit.setPlaceholderText(_translate("WardWindow", " New Password"))
        self.reconfirm_password_lineedit.setPlaceholderText(_translate("WardWindow", " Reconfirm New Password"))
        self.change_password_button.setText(_translate("WardWindow", "Change Password"))
        self.groupBox_2.setTitle(_translate("WardWindow", "Delete Account"))
        self.label.setText(_translate("WardWindow", " Enter password for deletion if you are to delete your account:"))
        self.deletion_password_lineedit.setPlaceholderText(_translate("WardWindow", " Enter password"))
        self.delete_account_button.setText(_translate("WardWindow", "Remove Account"))
        self.groupBox_3.setTitle(_translate("WardWindow", "Ward Profile"))
        self.municipality_update_lineedit.setPlaceholderText(_translate("WardWindow", " Municipality"))
        self.address_update_lineedit.setPlaceholderText(_translate("WardWindow", " Address"))
        self.email_update_lineedit.setPlaceholderText(_translate("WardWindow", " Email address"))
        self.phone_update_lineedit.setPlaceholderText(_translate("WardWindow", " Phone"))
        self.logo_path_update_lineedit.setPlaceholderText(_translate("WardWindow", " Logo path"))
        self.state_update_lineedit.setPlaceholderText(_translate("WardWindow", " State"))
        self.ward_no_update_lineedit.setPlaceholderText(_translate("WardWindow", " Ward No."))
        self.update_ward_profile_button.setText(_translate("WardWindow", "Update Ward Profile"))
        self.groupBox_4.setTitle(_translate("WardWindow", "Update Local Registrar Details"))
        self.update_registrar_button.setText(_translate("WardWindow", "Update Details"))
        self.registrar_name_lineedit.setPlaceholderText(_translate("WardWindow", "Name of Local Registrar"))
        self.registrar_post_lineedit.setPlaceholderText(_translate("WardWindow", "Post of the Local Registrar"))
        self.remove_registrar_button.setText(_translate("WardWindow", "Remove Registrar"))
import sw_rc

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WardWindow = QtWidgets.QMainWindow()
    ui = Ui_WardWindow()
    ui.setupUi(WardWindow)
    WardWindow.show()
    sys.exit(app.exec_())

