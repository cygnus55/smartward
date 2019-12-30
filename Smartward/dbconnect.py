import mysql.connector
class database:
    def __init__(self,hostname,user,dbase,pword=""):
        self.mydb=mysql.connector.connect(
            host=hostname,
            username=user,
            password=pword,
            database=dbase    
            )

    def insertintowadatable(self,name,address,about):
        mycursor=self.mydb.cursor()
        sql="INSERT INTO wada(wada_name,wada_address,wada_info) VALUES (%s,%s,%s)"
        val=(name,address,about)  
        mycursor.execute(sql,val)        
        self.mydb.commit()
        print("insert successful.")
        mycursor.close()
