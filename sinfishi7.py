import pymysql

class Mysql:
    def __init__(self):
        self.connectDB()
        self.CreateDB()
        self.CreateTB()

    
    def connectDB(self):
        self.db=pymysql.connect(
            host="localhost",
            user="root",
            password="1234"
        )
        self.c=self.db.cursor()
    def CreateDB(self):
        self.c.execute("create database if not exists Kompaniya")
        self.c.execute("use Kompaniya")


    def CreateTB(self):
        self.c.execute("""create table if not exists company (name varchar(50), 
                       location varchar(50), capital varchar(50), employees_count int,
                        establishAt int, monthly_expenses int)""")
        
    def insertcompanyTB(self, name, location, capital, employees, establishAt, monthly_expenses):
        self.c.execute(f'''insert into company values(
                       {name},{location},{capital}, {employees}, {establishAt}, {monthly_expenses})''')
        self.db.commit()
        

mysql=Mysql()

mysql.insertcompanyTB("apple", "USa", "New_York", 5000, 1980, 1000000)
# mysql.insertcompanyTB("samsung", "Korea", "Seul", 3000, 2000, 300000)
# mysql.insertcompanyTB("artel", "Uzbekiston", "Toshkent", 1200, 2019, 150000)
# mysql.insertcompanyTB("NIke", "Canada", "Ottava", 3900, 1990, 20000)
# mysql.insertcompanyTB("redme", "china", "pekin", 5000, 1997, 600000)



