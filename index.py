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

ussd = input('Ussd code: ')

if ussd == '*312#':
    print("""
        1. Buy data
        2. Check balance
        #. exit
    """)
    choice = input('Choice: ')
    if choice == '1':
        print('''
            1. Daily plan
            2. Weekly plan
            3. Monthly plan  
        
        ''')
        choice2 = input('Choice: ')
        
    elif choice == '2':
        print('Your balance is  1000mb')
    
    elif choice == '#':
        print('Bye Bye')
    
    else:
        print('Invalid input')    
else:
    print('Invalid ussd code.')
    
    
    
# val = 5
# if val == 5:
#     print('yes')
    
# else:
#     print('no')
    
# if val == 8:
    
    