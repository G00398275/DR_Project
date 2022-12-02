'''Data Representation - Winter 2022
Big Project: nflDAO.py
Author: Ross Downey (G00398275)
Lecturer: Andrew Beatty'''

import mysql.connector

from dbconfig import mysql as cfg

class NFL_DAO:
    host =""
    user = ""
    password =""
    database =""

    connection = ""
    cursor =""
    
    def __init__(self):
        self.host=       cfg['host']
        self.user=       cfg['user']
        self.password=   cfg['password']
        self.database=   cfg['database']

    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    def createDatabase(self):
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password   
        )
        self.cursor = self.connection.cursor()
        sql="create database "+ self.database
        self.cursor.execute(sql)

        self.connection.commit()
        self.closeAll()   

    def createtable(self):
        cursor = self.getcursor()
        sql="create table QBTable (id int AUTO_INCREMENT NOT NULL PRIMARY KEY, Name varchar(250), Team varchar(250), Passing_Yards int(5), TDs int(3), INTs int(3))"
        cursor.execute(sql)

        self.connection.commit()
        self.closeAll() 
         
    def createQBs(self, values):
        
       cursor = self.getcursor()
       sql="insert into QBTable (Name, Team, Passing_Yards, TDs, INTs) values (%s,%s,%s,%s,%s)"
       cursor.execute(sql, values)

       self.connection.commit()
       newid = cursor.lastrowid
       self.closeAll()
       return newid
        
    def convertToDictionary(self, result):
        pass
    '''
        colnames=['id','title','author', "price"]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
       '''
    def getAllQBs(self):
        cursor = self.getcursor()
        sql="select * from QBTable"
        cursor.execute(sql)
        result = cursor.fetchall()
        for x in result:
            print(x)
        self.closeAll()
        return result

    def findQBByID(self, id):
        cursor = self.getcursor()
        sql="select * from QBTable where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        for x in result:
            print(x)
        self.closeAll()
        return result

    def updateQBs(self, values):
        cursor = self.getcursor()
        sql="update QBTable set Name= %s, Team=%s, Passing_Yards=%s, TDs=%s, INTs=%s where id = %s"
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    def deleteQB(self, id):
        cursor = self.getcursor()
        sql="delete from QBTable where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll
        
nflDAO = NFL_DAO()

if __name__ == "__main__":
    #nflDAO.createDatabase()
    #print("Database created!")

    #nflDAO.createtable()
    #print("Table created!")

    #data = ("Josh Allen", "Buffalo Bills", 3183, 23, 11)
    #nflDAO.createQBs(data)
    #print ("QB Added to table!")

    nflDAO.getAllQBs()
    print ("All QBs in table are listed above")

    #nflDAO.findQBByID(1)
    #print ("The QB with id number given is listed")

    #values = ("Josh Allen", "Buffalo Bills", 4000, 30, 20, 2)
    #nflDAO.updateQBs(values)
    #print ("The QB with id number given has been updated with the values given")

    #nflDAO.deleteQB(2)
    #print ("The QB with the id number given has been deleted")
    
    print("(In)sanity!!")