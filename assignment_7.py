import psycopg2
def table():
    connect = psycopg2.connect(dbname= "postgres", user="postgres", password="Ank85@s1l", host="localhost", port="5432")

    cursor = connect.cursor()
    cursor.execute('''create table employees(Name Text, Id int, Age int);''')
    print("Table Created Successfully")

    connect.commit()
    connect.close()

def insert():
    connect = psycopg2.connect(dbname= "postgres", user="postgres", password="Ank85@s1l", host="localhost", port="5432")

    cursor = connect.cursor()
    cursor.execute('''insert into employees(Name,Id,Age)values('sunil',1234,21);''')
    print("Date Inserted Successfully")

    connect.commit()
    connect.close()

def extract():
    connect = psycopg2.connect(dbname= "postgres", user="postgres", password="Ank85@s1l", host="localhost", port="5432")

    cursor = connect.cursor()
    cursor.execute('''select * from employees;''')
    show = cursor.fetchone()
    print(show[0])

    connect.commit()
    connect.close()

def data():
    connect = psycopg2.connect(dbname= "postgres", user="postgres", password="Ank85@s1l", host="localhost", port="5432")

    cursor = connect.cursor()
    name = input('Enter name: ')
    id = input('Enter Id: ')
    age = input('Enter Age: ')
    query = '''insert into employees(Name,Id,Age) values(%s,%s,%s)'''
    cursor.execute(query, (name,id,age))
    print("Data Added Sucessfully")

    connect.commit()
    connect.close()

data()