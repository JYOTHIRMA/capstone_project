import mysql.connector


class Mysql_DBaccess:
    def __init__(self,host,user,password,db):
        self.host=host
        self.user=user
        self.password=password
        self.db=db
        try:
            self.connection=mysql.connector.connect(host=self.host,database=self.db,
                                                    user = self.user,password=self.password)
        except:
            print("error while connecting to the database")
    '''def insert_data(self,username,password):
        self.username=username
        self.password=password
        self.cur=self.connection.cursor()
        sql="insert into user(username,passwd) values(%s,%s);"
        val=(self.username,self.password)'''
    def inser_data(self,filename):
        self.filename=filename
        self.cur=self.connection.cursor()
        sql="insert into files(filename) values(%s)"
        val=(self.filename)

        self.cur.execute(sql,(val,))
        self.connection.commit()

    def searchDB(self, fil):
        self.f = "filename"

        sql = """select * from files where filename like '%{0}'""".format(fil)
        self.cur.execute(sql)
        row = self.cur.fetchone()
        if row == None:
            return 0
        else:
            print(row)

    def search(self):
        self.cur=self.connection.cursor()
        sql="SELECT * FROM files limit 0,103"
        data=self.cur.execute(sql)
        data=self.cur.fetchall()
        return data
dbobj=Mysql_DBaccess('localhost','root','jyothi@123','searchfiles')
dbobj.inser_data('c://hcl//demo.txt')
dbobj.searchDB('c://hcl//demo.txt')

