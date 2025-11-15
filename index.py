# print("Good morning everyone!")

# commenting 
# block and  inline comment
'''
Hello, this is python class note
I hope it will be helpful 
'''

# print("It's")
# print(' this is "quoted" ')

# print("""
#             1. Buy data
#         2. Check balance
# """)

# print("1. Buy Data")
# print("2. check Data")

# Identation

# Variable

username = "Damilare"
age = 20
occupation = 'Software Engineer'

# firstNameOfUser = ''
# FirstNameOfUser = ''
# first_name_of_user = ''



# print(username)

students = "Stephen", 'Aisha', 'Isaac'
# print(students)

# x = y = z = 10
# y = y - 2
# print(x)

student1, student2, student3 = 'Bolu', 'Blessing', 'Samuel'
# print(student2)


# concatenation

# print(type(age))

# print('My name is ' + username + ' I am ' + str(age) + 'years old') 

# print('My name is', age)

# print(f"My name is {username}. I am {age}years old.")

# firstname = input('Firstname: ')
# print(firstname)


# Python datatypes
# 1. Number type; e.g Int, Float, Complex
# 2. text type; string
# 3. sequence type; list [], tuple (), range()
# 4. mapping type: dict 
# 5. boolean: True, False
# 6. set type
# 7. none type
# 8. binary type; byte, bytearray, memoryview

num1 = 10
num2 = 10.5
num3 = 10 + 2j

text = "How are you"
market = ['rice', 'beans', 'pepper', 'tomato', 'chicken']
# print(market)

# var = range(0, 10, 2)
# print(list(var))

# student = {
#     'name': 'Kenny',
#     'course': 'AI',
#     'address': 'Lagos'
# }

# print(student['address'])
# print(type(var))

# available = False
# print(type(available))

setA = {'apple', 'mango', 'orange'}
setB = {2, 4, 5, 7, 6, 3, 1}
# print(setB)

name = None
# print(type(name))

# val1 = 'three'
# val2 = int(val1)
# print(type(val2))

on = None
# print(bool(on))



# python operators
# 1. Arithmetic: +, -, *, /, //, %, **
# print(5 ** 2)

# 2. Assignment: =, +=, -=, /=, *=, //=  e.t.c
# val = 5
# val += 1 # val = val + 1
# val -= 2
# print(val)

# 3. comparison; ==, !=, >, <, >=, <=
val = 5
# print(val >= 5)

# 4. logical operator; and, or, not

# AND
'''
A   B   AND     OR      NOT B       XOR
0   0   0       0       1           0
1   0   0       1       1           1
0   1   0       1       0           1
1   1   1       1       0           0

'''
 
# 5. Membership operator; in,  not in
menu = ['rice', 'yam', 'amala', 'ofe nsala']
# print('Yam' not in menu)

# 6. Identity operator; is, is not
val = 5
num = 5
# print(val is not num)

# 7. bitwise operator: 
'''
    & -> AND
    | -> OR
    ~ -> NOT
    ^ -> XOR
'''
# print(bin(20))
# print(bin(10))          # 1 0 1 0
# print(bin(5))           #   1 0 1
# print(bin(10 & 5))      # 0 0 0 0
# print(bin(10 | 5))
# print(bin(10 ^ 5))



# conditional statement(if/else)

# val = 12

# if val == 5:
#     print('yes!! val is 5')

# elif val == '5':
#     print('Val is 5 but a string type')

# else:
#     print('so sorry val is not 5')


# Class work
# 1. Write a contional that tells if the number supplied is fizz or buzz or fizzbuzz

# Assignment
# 1. Build a simple calculator


# val = int(input('your number: '))

# if val % 2 == 0:
#     print('Even')
# else: 
#     print('Odd')

# nested conditional statement

# ussd = input('Ussd code: ')

# if ussd == '*312#':
#     print("""
#         1. Buy data
#         2. Check balance
#         #. exit
#     """)
#     choice = input('Choice: ')
#     if choice == '1':
#         print('''
#             1. Daily plan
#             2. Weekly plan
#             3. Monthly plan  
        
#         ''')
#         choice2 = input('Choice: ')
        
#     elif choice == '2':
#         print('Your balance is  1000mb')
    
#     elif choice == '#':
#         print('Bye Bye')
    
#     else:
#         print('Invalid input')    
# else:
#     print('Invalid ussd code.')
    
    
    
# val = 5
# if val == 5:
#     print('yes')
    
# else:
#     print('no')
    
# if val == 8:


# python strings 

name = "<//arise damilare%**" # ['A', 'r', 'i', 's', 'e', ' ', ....]
# print(type(name))
# print(len(name))
# print(name[5])
# print(name[-2])
# print(name[6:10])  #slicing

# print(ord('a'))
# print(chr(65))

# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.title())

# ques = "What is the Capital of Nigeria?"
# print(ques)
# ans = input('Ans: ')
# if ans.lower().strip() == 'abuja':
#     print('correct. you sabi')
# else:
#     print('Olodo.')


# print(len(name.strip()))

# print(name.lstrip('</%*'))
# print(name.rstrip('</%*'))


var = 'Welcome. This is AI and Datascience Dept. ai Your are currntly in leve 2. python class ai'
# print(var.split())
# print(var.split('.'))

#  word counter
# text = input('Enter your essay: ')
# if text == '':
#     print('No essay inputed. Kindly enter an essay')
# else:
#     splitted = text.strip().split()
#     print(f'Total word: {len(splitted)}')
    
    
splitted = ['I', 'am', 'happy', 'to', 'be', 'here']
# print('+'.join(splitted))

# print(var.endswith('Class')) 
# print(var.lower().startswith('welcome'))

# print(var.find('pythons'))

#  find if the sentence contains ai, datascience and python

# words = ['ai', 'datascience', 'python']

# if  'ai' in var.lower():
#     print('Valid')
# else:
#     print('invalid')

# var = var.lower()
# print(var.find('ai', 88))


# if var.find('ai') != -1 and var.find('datascience') != -1:
#     print('found')
# else:
#     print('not found')


# if var.find('ai') != -1 and var.find('datascience') != -1 and var.find('python') != -1:
#     print('Found')
# else:
#     print('Not found')

# class work 
# Write a system that verifies if an email is valid or not

# Assignment 
# 1. build a simple cbt application  
# 2.  build a simple grading system  
# A - 70 - 100
# B - 60 - 69
# C - 50 - 59
# D - 45 - 49
# E - 40 - 44
# F - 0 - 39
 
    
# Special character
# print('I am \\b\\bhappy')

# print('C:\\python_oct\\index.py')
# print('it\'s mine')

print(r'C:\python_oct\index.py')

# '\n' -> next line
# '\t' -> tab
# '\r' -> return 
# '\b' -> backspace
# '\' -> escape character


