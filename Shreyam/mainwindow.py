from ui_mainwindow import *

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WardWindow = QtWidgets.QMainWindow()
    ui = Ui_WardWindow()
    ui.setupUi(WardWindow)
    WardWindow.show()

    def on_home_button_clicked():
        ui.stackedWidget.setCurrentIndex(0)
    
    def update_profile():
        #update profile
        print("update profile")
        ui.stackedWidget.setCurrentIndex(1)
    
    def change_destination_folder():
        #change destination folder
        print("change destination folder")
        ui.stackedWidget.setCurrentIndex(2)
    
    def birth_reg():
        #birth registration
        #new Window-birth reg. form
        print("birth registration")
    
    def death_reg():
        #death registration
        #new Window-death reg. form
        print("death registration")

    def marriage_reg():
        #marriage registration
        #new Window-marriage reg. form
        print("marriage registration") 

    def divorce_reg():
        #divorce registration
        #new Window-divorce reg. form
        print("divorce registration") 

    def migration_reg():
        #migration registration
        #new Window-migration reg. form
        print("migration registration") 

    ui.home_button.clicked.connect(on_home_button_clicked)
    
    settings_menu=QtWidgets.QMenu()
    settings_menu.addAction("Update Profile",update_profile)
    settings_menu.addAction("Change Destination Folder",change_destination_folder)
    ui.settings_button.setMenu(settings_menu)
    
    vital_reg_menu=QtWidgets.QMenu()
    vital_reg_menu.addAction("Birth registration",birth_reg)
    vital_reg_menu.addAction("Death registration",death_reg)
    vital_reg_menu.addAction("Marriage registration",marriage_reg)
    vital_reg_menu.addAction("Divorce registration",divorce_reg)
    vital_reg_menu.addAction("Migration registration",migration_reg)
    ui.vital_reg_button.setMenu(vital_reg_menu)

    sys.exit(app.exec_())
