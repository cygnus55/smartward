import mysql.connector

class database:
    def __init__(self,hostname,user,dbase,pword=""):
        try:
            self.mydb=mysql.connector.connect(
                host=hostname,
                username=user,
                password=pword,
                database=dbase    
                )
        except Exception as e:
            print("Not connected to database.")

    def insertintowadatable(self,name,address,about):
        #INSERT INTO `smartward`.`ward_registration` (ID,Municipality,WardNo,State,Address,Phone,Email,IP_Address,LogoPath,Password) VALUES('1','A','B','2','sgjkf','8935734','C','576','231','123')
        mycursor=self.mydb.cursor()
        sql="INSERT INTO wada(wada_name,wada_address,wada_info) VALUES (%s,%s,%s)"
        val=(name,address,about)  
        mycursor.execute(sql,val)        
        self.mydb.commit()
        print("insert successful.")
        mycursor.close()

class database_signinwindow(database):
    def __init__(self,hostname,user,dbase,pword=""):
        super().__init__(hostname,user,dbase,pword)
        self.mycursor=self.mydb.cursor()

    def createWardTable(self):
        try:
            #"CREATE TABLE `departments` ("" `dept_no` char(4) NOT NULL,"" `dept_name` varchar(40) NOT NULL,"" PRIMARY KEY (`dept_no`), UNIQUE KEY `dept_name` (`dept_name`)"") ENGINE=InnoDB"
            sql="CREATE TABLE `smartward`.`ward_registration` ( `ID` VARCHAR(30) NOT NULL , `Municipality` VARCHAR(75) NOT NULL , `WardNo` VARCHAR(5) NOT NULL , `State` VARCHAR(5) NOT NULL , `Address` VARCHAR(150) NOT NULL , `Phone` VARCHAR(15) NOT NULL , `Email` VARCHAR(50) NOT NULL , `IP_Address` VARCHAR(15) NOT NULL , `LogoPath` VARCHAR(150) NOT NULL , `Password` VARCHAR(16) NOT NULL , PRIMARY KEY (`ID`)) ENGINE = InnoDB"
            self.mycursor.execute(sql)
            self.mydb.commit()
            print("table created.")
            self.mycursor.close()
        except Exception as e:
            print("table already exists")

    def checkValid(self,municipality,ward):
        sql="SELECT * FROM `smartward`.`ward_registration` WHERE Municipality=%s AND WardNo=%s"
        self.mycursor.execute(sql,(municipality,ward))
        if(self.mycursor.fetchall()):
            return False
        return True

    def checkEmailValid(self,email):
        sql="SELECT * FROM `smartward`.`ward_registration` WHERE Email=%s"
        self.mycursor.execute(sql,(email,))
        if(self.mycursor.fetchall()):
            return False
        return True

    def InsertIntoward_registrationTable(self,id,municipality,wardno,state,address,phone,email,ip,logopath,pword):
        try:
            sql="INSERT INTO `smartward`.`ward_registration` (ID,Municipality,WardNo,State,Address,Phone,Email,IP_Address,LogoPath,Password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val=(id,municipality,wardno,state,address,phone,email,ip,logopath,pword)
            self.mycursor.execute(sql,val)
            self.mydb.commit()
            self.mycursor.close()
            return True
        except Exception:
            print("insert failed")
            return False

    def checkLoginValidity(self,id,pswd):
        sql = "SELECT * FROM `smartward`.`ward_registration` WHERE ID=%s OR Email=%s"
        self.mycursor.execute(sql, (id,id))
        login_details=self.mycursor.fetchall()
        if(login_details):
            if(pswd==login_details[0][-1]):
                return login_details[0][-3],login_details[0][-4],login_details[0][0]
        return "invalid","",""

    def checkEmailValidity(self,email):
        sql = "SELECT * FROM `smartward`.`ward_registration` WHERE Email=%s"
        self.mycursor.execute(sql, (email,))
        return self.mycursor.fetchall()

    def updateIP(self,id,ip):
        try:
            sql="UPDATE `smartward`.`ward_registration` SET IP_Address=%s WHERE ID=%s OR Email=%s"
            self.mycursor.execute(sql,(ip,id,id))
            self.mydb.commit()
            self.mycursor.close()
        except Exception:
            print("Ip update unsucessful")
