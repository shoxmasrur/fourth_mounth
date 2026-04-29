import pymysql

class Mysql:
    def __init__(self):
        self.connection()
        self.CreateDB()
        self.CreateTB()
    

    def connection(self):
        
        self.db=pymysql.connect(
            host="localhost",
            user="root",
            password="1234"
        )

        self.c=self.db.cursor()

    def CreateDB(self):
        self.c.execute("""create database if not exists uy_ish_2""")
        self.c.execute("""use uy_ish_2""")

    def CreateTB(self):
        self.c.execute("""create table if not exists restaranlar (id int auto_increment,
                       name varchar(40), address varchar(40), maxFoodPrice int, minFoodPrice int, 
                       employeesCount int, experience int)""")
    
    def InsertTB(self):
        self.c.execute("""insert into restaranlar(name, address, maxFoodPrice, minFoodPrice, 
                       employeesCount, experience) values('Buxoro taomlari', 'Yunusobot tumani', 
                       200000, 20000, 30, 10 )""")
        self.c.execute("""insert into restaranlar(name, address, maxFoodPrice, minFoodPrice, 
                       employeesCount, experience) values('Feed up', 'Yunusobot tumani', 
                       100000, 15000, 14, 3 )""")
        self.c.execute("""insert into restaranlar(name, address, maxFoodPrice, minFoodPrice, 
                       employeesCount, experience) values('SAZANCHIK', 'Yakkasaroy tumani', 
                       530000, 30000, 55, 4 )""")
        self.c.execute("""insert into restaranlar(name, address, maxFoodPrice, minFoodPrice, 
                       employeesCount, experience) values('Xorazm baliq', 'chilonzor tumani', 
                       600000, 25000, 17, 9 )""")
        self.c.execute("""insert into restaranlar(name, address, maxFoodPrice, minFoodPrice, 
                       employeesCount, experience) values('Bahor', 'Mirzo Ulugbek tumani', 
                       80000, 10000, 90, 7 )""")
        self.c.execute("""insert into restaranlar(name, address, maxFoodPrice, minFoodPrice, 
                       employeesCount, experience) values('Beshbarmoq', 'chilonzor tumani', 
                       500000, 50000, 76, 13 )""")
        self.c.execute("""insert into restaranlar(name, address, maxFoodPrice, minFoodPrice, 
                       employeesCount, experience) values('uchbaqaloq', 'Olmazor tumani', 
                       400000, 40000, 32, 20 )""")
        self.c.execute("""insert into restaranlar(name, address, maxFoodPrice, minFoodPrice, 
                       employeesCount, experience) values('Fayz', 'Olmos tumani', 
                       200000, 20000, 35, 10 )""")
        self.c.execute("""insert into restaranlar(name, address, maxFoodPrice, minFoodPrice, 
                       employeesCount, experience) values('Salom kafe', 'Yunusobot tumani', 
                       340000, 13000, 67, 18 )""")
        self.c.execute("""insert into restaranlar(name, address, maxFoodPrice, minFoodPrice, 
                       employeesCount, experience) values('Buxoro taomlari', 'Uchtepa tumani', 
                       450000, 30000, 56, 19 )""")
        self.db.commit()

    def firstQuery(self):
        self.c.execute("""select * from restaranlar where name like 'B%' and name like '%I' order by maxFoodPrice""")
        return self.c.fetchall()
    def secentdQuery(self):
        self.c.execute("""select * from restaranlar order by minFoodPrice""")
        return self.c.fetchmany(3)
    
    def thirdQuery(self):
        self.c.execute("""select * from (select * from restaranlar order by experience desc) t order by maxFoodPrice limit 4""")
        return self.c.fetchall()

       
mysql=Mysql()
# mysql1.InsertTB()

# 1-shart Nomi B bilan boshlanib, I bilan tugaydigan restoranlarni maxFoodPricega kora osish tartibida chiqaring.
# natija=mysql.firstQuery()
# for i in natija:
#     print(i)

    # 2-shart Eng kam pulga ovqatlansa boladigan 3ta restoran nomini chiqaring.
# natija=mysql.secentdQuery()
# for i in natija:
#      print(i)




# 3-shart.  Tajribasi bo'yicha kamayish tartibida sortlangan restoranlarni eng qimmatga ovqatlanish mumkin bo'lgan 
#             4ta restoran nomini va eng qimmat taom narxini chiqaring.

# natija=mysql.thirdQuery()
# for i in natija:
#     print(i)


