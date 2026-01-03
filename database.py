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
    password="password"
)

mycursor = conn.cursor()

# mycursor.execute("DROP DATABASE bank_db")
mycursor.execute("CREATE DATABASE bank_db")