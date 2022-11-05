import mysql.connector as connector
 
class DBHelper:
    def __init__(self):
        self.con=con=connector.connect(host='localhost', port='3306', user='root', password='rahul', database='pythontest')
        query='create table if not exists user(userId int primary key, userName varchar(200), phone varchar(12))'
        cur=self.con.cursor()
        cur.execute(query)
        print("Created")
    
    def insert_user(self, userId, userName, phone):
        query="insert into user(userId, userName, phone)values({},'{}','{}')".format(userId, userName, phone)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to db")

    def fetch_all(self):
        query="select * from user"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print(row)



    def fetch_one(self, id):
        query="select * from user where userId='{}'".format(id)
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print(row)


    def delete(self, id):
        query="delete from user where userId='{}'".format(id)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("deleted")


    def update_user(self, userId, newName, newPhone):
        query="update user set userName='{}', phone='{}' where userId={} ".format(newName, newPhone, userId)
        print (query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")


helper=DBHelper()
helper.delete(144)
helper.fetch_all()