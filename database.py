'''
Database management systems

Types of DBMs
1. Relational DBMs or SQL (Structured Query Language)
    i. It works with structured (Tabular form) data
    ii. It helps create table relationships using keys
    
Database - Table

s/n     name        gender
1       Adebayo     Male

examples: MySQL, Oracle, Postgres, SQLLITE, MSSQL. MARIABD

catategories of SQL queries
1. DDL (Data Definition language) e.g CREATE, DROP, ALTER, TRUNCATE
2. DML (Data Manipulation Language) e.g UPDATE, INSERT, DELETE
3. DQL (Data Query Language) e.g SELECT

2. Non Relational DBMs or NoSQL
    i. Unstructured or semi-structured data
    
    
    {
        name => Adebayo
        gender => Male
    }
    
    example: MongoDB, Redis, Firebase realtime database

'''

# mysql-connector

import mysql.connector as sql

conn = sql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="password",
    database = 'bank_db'
)
conn.autocommit = True
mycursor = conn.cursor()

# mycursor.execute("DROP DATABASE bank_db")
# mycursor.execute("CREATE DATABASE bank_db")
# mycursor.execute("""
#         CREATE TABLE users(
#             id INT PRIMARY KEY AUTO_INCREMENT,
#             fullname VARCHAR(50),
#             email VARCHAR(50) UNIQUE,
#             password VARCHAR(50),
#             account_no VARCHAR(10) UNIQUE, 
#             balance FLOAT(10,2) DEFAULT 0.00,
#             date_created DATETIME DEFAULT CURRENT_TIMESTAMP
#         )        
#     """)

# ALTER CHANGE, ALTER ADD, ALTER DROP

# mycursor.execute("ALTER TABLE users DROP COLUMN email")
# mycursor.execute("ALTER TABLE users ADD COLUMN email VARCHAR(50) UNIQUE AFTER fullname")
# mycursor.execute("ALTER TABLE users CHANGE COLUMN date_created created_at  DATETIME DEFAULT CURRENT_TIMESTAMP")

# mycursor.execute("INSERT INTO users(fullname, email, password, account_no) VALUES('Arise Damilare', 'dami@gmail.com', '1234', '0987654321')")


# query = "INSERT INTO users(fullname, email, password, account_no) VALUES(%s, %s, %s, %s)"

# values = ('DAMI Damilare', 'dami2@gmail.com', '1234', '0987654322')
# mycursor.execute(query, values)

# conn.commit()
import random

def get_password():
    password1 = input('Password: ')
    password2 = input("Confirm password: ")
    if password1 == password2:
        return password1
    else:
        print('Password do not match. Try again')
        return get_password()


def create_account():
    fullname = input('Fullname: ')
    email = input('Email: ')
    password = get_password()
    account_no = random.randint(2000000000, 2099999999)
    
    query = "INSERT INTO users(fullname, email, password, account_no) VALUES(%s, %s, %s, %s)"
    values = (fullname, email, password, account_no)
    mycursor.execute(query, values)
    print('Registration Successful')
    
# create_account()


# query = "UPDATE users SET balance = %s WHERE id=%s"
# values = (2000, 2)
# mycursor.execute(query, values)

# query = "DELETE FROM users WHERE id=%s"
# values = (6,)
# mycursor.execute(query, values)


# mycursor.execute('SELECT * FROM users')
# mycursor.execute('SELECT fullname, email FROM users')
# print(mycursor.fetchall())
# mycursor.execute('SELECT fullname, email, account_no, balance FROM users WHERE email="dami@gmail.com" AND password = "12345"')
# print(mycursor.fetchone())

def login():
    email = input("Email: ")
    password = input("Password: ")
    
    query = 'SELECT fullname, email, account_no, balance FROM users WHERE email=%s AND password=%s'
    
    values = (email, password)
    
    mycursor.execute(query, values)
    
    details = mycursor.fetchone()
    
    if details:
        print('Login Succesfull')
        print(details)
    else:
        print('Incorrect email or password')

# login()

# Build A todo and integrate SQL to it. 

