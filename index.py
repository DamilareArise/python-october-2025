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

# print(r'C:\python_oct\index.py')

# '\n' -> next line
# '\t' -> tab
# '\r' -> return 
# '\b' -> backspace
# '\' -> escape character


# Python collections / Array

# 1. List - [] or list()
# A list is ordered, changeable or mutable, indexed, allows duplicate values
fruits = ['Apple', 'Pineapple', 'Banana', 'Agbalumo', 'Pawpaw', 'Banana']
# print(type(fruits))
# print(len(fruits))
# print(fruits[-2])
# print(fruits[1:4])
# print(fruits[-5:-1])
# print(fruits[2:])
# print(fruits[:4])

# fruits[2] = 'Tomato'
# print(fruits)

# var = 'Tomato'
# print(var[0])
# var[0] = 'X'

# fruits[0][0]


# fruits.append('Tomato')
# fruits.insert(0, 'Tomato')
# fruits.extend(['Rice', 'Beans'])

# fruits.pop(0)
# fruits.remove('Pineapple')
# fruits.clear()
# print(fruits.index('Banana', 3))
# fruits.reverse()

# print(fruits) 

num = [1, 3, 5, 6]
# print(sum(num))
# print(min(num))
# print(max(num))

# LOOP 
# 1. For loop

# for fruit in fruits:
#     print(fruit, 'is a kind of fruit.')

# print(list(range(0, 10, 2)))

# for x in range(10):
#     print(x)

# for x in range(1, 6):
#     print(f'\n{x} Times table\n')
#     for y in range(1, 13):
#         print(f'{x} X {y} = {x*y}')

# print('Welcome to my Todo application')  
# database = []

# for x in range(100):

#     print('''    
#         1. Add a todo
#         2. Delete a todo
#         3. Edit
#         4. view
#         5. clear all
#         #. Exit
#     ''')

#     choice = input('Choice: ').strip()
#     if choice == '1':
#         todo = input('Todo: ').strip().capitalize()
#         if todo == '':
#             print('Todo can not be empty!')
#         else:
#             database.append(todo)
#             print('Todo added!')

#     elif choice == '2':
#         pass
    
#     elif choice == '4':
#         if database == []:
#             print('No Todo Yet!')
#         else:
#             num = 1
#             for x in database:
#                 print(f'{num}. {x}')
#                 num += 1
            
#     elif choice == '#':
#         print('Bye!')
#         exit()
        
#     else:
#         print('Invalid Choice.')
        
        
# class work. 
# https://www.99-bottles-of-beer.net/lyrics.html using for loop

# Assigment.
# 2. Complete the todo application 

# 2. While loop

# 2. Tuple '()' - Indexed, ordered, unchangeable|immutable , allows duplicate values 
fruits = ('Apple', 'Orange', 'Apple', 'Cherry')

# print(type(fruits))
# print(len(fruits))
# print(fruits[0][0])
# print(fruits[0:2])

# fruits[0] = 'Pineapple' # error.
# print(fruits.count("Orange"))
# print(fruits.index('Cherry'))

# fruits_list = list(fruits)
# fruits_list[0] = 'Pineapple'
# print(fruits_list)
# fruits = tuple(fruits_list)
# print(fruits)

# Unpacking
# a, b, c, d  = fruits
a, *d, e  = fruits
# *a, b, c = fruits
# *fruits_list, = fruits
# print(fruits_list)
# fruits_list[0] = 'Pineapple'
# fruits = tuple(fruits_list)
# print(fruits)

score = 0

# print('1. What is the capital of Nigeria.  \na.) Abuja .b)Lagos')
# ans = input('Ans: ').strip().lower()
# if ans == 'a':
#     score += 1
#     print('Correct')
    


questions = [
    '1. What is the capital of Nigeria.  \na.) Abuja .b)Lagos',
    '2. What is the Capital of Ghana. \na.) Accra .b)Lagos'
]

answers = ['a', 'a']
mark = [5, 10]

# for ques, ans, mrk in zip(questions, answers, mark):
#     print(ques) 
#     user_ans = input('Ans: ').strip().lower()
#     if user_ans == ans:
#         print('Correct\n')
#         score += mrk
#     else:
#         print('Wrong\n')

# print(f'Total score is {score}/{sum(mark)}')

# exams = [
#     ('1. What is the capital of Nigeria.  \na.) Abuja .b)Lagos', 'a', 2),
#     ('2. What is the Capital of Ghana. \na.) Accra .b)Lagos', 'a', 4),
#     ('3. What is the capital of Japan. \na.) Japan b.) Tokyo', 'b', 5)
# ]

# for ques, ans, mrk in exams:
#     print(ques)
#     user_ans = input('Ans: ').strip().lower()
#     if user_ans == ans:
#         print('Correct\n')
#         score += mrk
#     else:
#         print('Wrong\n')

# print(f'Total score is {score}')
    

# 3. Set {} | set() - unordered, unchangeable|immutable, can't be indexed, doesn't allow duplicate
fruits = {'Apple', 'Orange', 'Apple', 'Cherry'}
# print(fruits[0])
# fruits.add('Mango')
# fruits.remove('Orange')
# fruits.discard('Oranges')

# fruits.update(['Mango', 'Tomato'])
# fruits.clear()
# print(fruits)
fruits.pop()
# print(fruits)
# db = set()

setA = {2, 3, 4, 7, 8, 9, 1, 5, 6}
setB = {13, 4, 3, 2, 5, 12, 10, 11}
setC = {1, 2, 4}
setD = {20, 21}
# print(setA)
# print(setA.union(setB))
# print(setA.intersection(setB))
# print(setA.difference(setB))
# print(setA.symmetric_difference(setB))

# setA.intersection_update(setB)
# print(setA)

# print(setA.issubset(setC))
# print(setA.issuperset(setC))
# print(setA.isdisjoint(setD))




# 4. Dictionary {}
person = {
    'last_name': 'Edun',
    'first_name': 'Boluwatife',
    'course': 'Data Science',
    'height': 5.7,
    # 'location': {
    #     'street': 'Onward way',
    #     'city': 'Ikeja',
    #     'state': 'Lagos',
    #     'geo': {
    #         'lat': 123,
    #         'lon': 456
    #     }
    # }
}

# print(person['last_names'])
# print(person.get('last_name', 'Not Found'))
# person.pop('course')

# print(person)
# person.update({'course': 'AI', 'location': 'Lagos'})
# print(person['location']['geo']['lat'])

# print(person.values())
# print(person.items())

# for key, val in person.items():
#     print(key, val)


exams = {
    '1. What is the capital of Nigeria.  \na.) Abuja .b)Lagos': 'a',
    '2. What is the Capital of Ghana. \na.) Accra .b)Lagos': 'a',
}

# for ques, ans in exams.items():
#     print(ques)


# Assignment 
db = ['eat', 'sleep']

db = [
    {'todo': 'Eat', 'completed': False},
]
# Build a todo app using the structure above0



# WHILE LOOP

# x = 5
# while x > 0:
#     print('Hello', x)
#     x -= 1

# x = 0 
# while x < 10:

#     # if x == 7:
#     #     break
#     x+=1  
#     if x == 7:
#         continue
    
#     print('Hello', x)
      
# else:
#     print('Done')


# tickets = 10

# while tickets > 0:
#     age = int(input('Age: '))
#     if age < 18:
#         print('Too young. come back next year!')
#         continue
    
#     if tickets == 3:
#         print(tickets, 'Reserved.')
#         break
    
#     tickets -= 1
#     print('Take your ticket. remaining', tickets)
    
# else:
#     print('No more ticket.')   

database = []
print('Welcome to MyTodo')
while True:
    print('''
        1. Add Todo
        2. Delete Todo
        3. View Todo
        4. Mark as completed
        #. Exit
    ''')
    choice = input('Choice: ').strip()
    if choice == '1':
        todo = input('Input Your Todo: ').strip().capitalize()
        if not todo:
            print('Kindly input a todo')
            continue
        
        todo_obj = {
            'todo': todo,
            'completed': False
        }
        database.append(todo_obj)
        print('Todo added successfully')
        
    elif choice == '2':
        pass
    
    elif choice == '3':
        # print(database)
        no = 1
        for data in database:
            todo = data['todo']
            status = data['completed']
            print(f"{no}. {todo} - {'[Completed]' if status else '[Not Completed]'} ")

            no += 1 
        
        
    elif choice == '4':
        num = int(input('Complete todo number? '))
        if num > len(database) or num < 1:
            print('Invalid Selection')
            continue
        
        database[num -1]['completed'] = True
        print('Done!')     
    
    elif choice == '#':
        print('Good Bye!')
        exit()
    
    else:
        print('Invalid Input')
    
    