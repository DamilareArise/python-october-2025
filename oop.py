# OOP - object oriented programming 

def home():
    global val1, val2
    
    val1 = int(input('val1: '))
    val2 = int(input('val2: '))
    print('''
        1. Add
        2. Subtract
        #. Exit
    ''')
    choice = input('Choice: ')
    if choice == '1':
        add()
    if choice == '2':
        sub()
    if choice == '#':
        exit()
    
def add():
    print('Result:', val1 + val2)
    home()
    
def sub():
    print('Result:', val1 - val2)
    home()


# home()



class Male:  # declaration
    # definition - includes the properties amd function of the class
    __name = 'Damilare' # private encapsulation type
    hobby = 'Singing' # public 
    
    def talk(self):
        print(f'{self.__name} can talk. I love {self.hobby}')
        self.walk()
    
    def walk(self):
        print('I am walking')


# dami = Male()  # invocation - Where the instance of the class is created e.g dami
# sam = Male()

# dami.hobby = 'Swimming'
# dami.talk()
# sam.talk()
# print(dami.hobby)



# print(type(dami))

# var = list()
# var.append
# print(type(var))

# num = 5




class Calculator:
    __name = None
    color = None
    inp1 = 0
    inp2 = 0
    
    def __init__(self, name, color):
        self.__name = name
        self.color = color
        # print('Hello')
        self.getName()
    
    def add(self):
        print('Result: ', self.inp1 + self.inp2)
        
    def sub(self):
        print('Result: ', self.inp1 - self.inp2)
        
    def getName(self):
        print(self.__name)
        
    def setName(self, new_name):
        self.__name = new_name
        print('Done')

# myCal = Calculator('Cascio', 'Yellow')#
# myCal.inp1 = 5
# myCal.inp2 = 10
# myCal.add()
# myCal.getName()

# samCalc = Calculator()
# samCalc.color = 'White'
# samCalc.__name = 'Porpo'

# samCalc.setName('Porpo')
# samCalc.getName()



class Bank:
    __name = None
    __balance = 0
    
    def __init__(self, bank_name):
        self.__name = bank_name
        print(f'Welcome to {self.__name}')
        self.home()
        
    
    def home(self):
        print('''
            1. Deposit
            2. Withdraw
            3. Check balance
            #. Exit
        ''')
        
        choice = input('Choice: ')
        if choice == '1':
            self.deposit()
        
        elif choice == '2':
            self.withdraw()
            
        elif choice == '3':
            self.check_balance()
        
        elif choice == '#':
            print('Goodbye!')
            exit()
        
        else:
            print('Invalid Input')
            self.home() 
            
    def deposit(self):
        amount = float(input('Amount: '))
        if amount < 1:
            print('Amount can\'t be less than 1') 
            self.deposit()
            
        self.__balance += amount
        print(f'#{amount:,} deposited successfully. Your balance is #{self.__balance:,}')
        
        self.home()
        
        
    def withdraw(self):
        amount = float(input('Amount: '))
        if amount < 1:
            print('Amount can\'t be less than 1') 
            self.withdraw()
        elif self.__balance < amount:
            print('Insufficient fund')
            self.home()
            
        self.__balance -= amount
        print(f'#{amount:,} withrawn successfully. Your balance is #{self.__balance:,}')
        
        self.home()
        
    def check_balance(self):
        print(f'Your Balance is #{self.__balance:,}')
        self.home()
            
        
        
# uba = Bank('UBA')


# Inheritance
f_name = 'Ayo'

class Human:
    sex = 'Male'
    f_name = None
    l_name = None

    
    def __init__(self, first_name, last_name):
        self.f_name = first_name # 'Adewale'
        self.l_name = last_name # 'Ayuba
        # print('Welcome')
    
    def intro(self):
        print(f'My name is {self.f_name} {self.l_name}')


# person1 = Human('Adewale', 'Ayuba') 
# print(person1.sex)
# person1.intro()


# person2 = Human()


class Child(Human):
    hobby = None
    
    def __init__(self, first_name, last_name, hobby):
        super().__init__(first_name, last_name)
        self.hobby = hobby

    def likes(self):
        print(f'I like {self.hobby}')

# child1 = Child('Adeniyi', 'Stephen', 'Coding')
# print(child1.sex)
# child1.intro()
# child1.likes()




    
    
# Frontend

# import config
# from config import BankConfig # if they are in the same folder
from modules.config import BankConfig as BK



# class BankFrontend(config.BankConfig):
class BankFrontend(BK):
    
    def __init__(self, bank_name):
        super().__init__(bank_name)
        print(f'\nWelcome to {self.name}')
    
    def home(self):
        print('''
            1. Deposit
            2. Withdraw
            3. Check Balance 
            #. Exit
        ''')
        
        choice = input('Choice: ')
        if choice == '1':
            self.deposit()
            
        elif choice == '2':
            self.withdraw()
        
        elif choice == '3':
            self.check_balance()
        
        elif choice == '#':
            print('Goodbye!')
            exit()
        else:
            print('Invalid input')
            self.home()
        
    def deposit(self):
        amount = float(input('Amount: '))
        resp = self.perform_deposit(amount)
        
        print(resp['message'])
        
        if resp['status']:
            self.home()
        else:
            self.deposit()
            
    def withdraw(self):
        amount = float(input('Amount: '))
        resp = self.perform_withdraw(amount)
        
        print(resp['message'])
        
        if resp['status']:
            self.home()
        else:
            self.withdraw()
            
    def check_balance(self):
        print(f'Your balance is ${self.get_balance()}')    
        self.home()
        
        
        
# bank1 = BankFrontend('MyBank')
# bank1.home()


# Modularization
# 1. Python Scripts
# 2. Modules # time
import time, datetime as dt, random as rd

# print('Loading...')
# time.sleep(3)
# print('Done')

# print(dt.datetime.now())

# print(rd.random() * 100000)
print(rd.randint(2000000000, 2099999999))



# 3. Library # pandas, numpy,
# import pandas as pd
 
# 4. Frame work # seaborn, Django, fastApi


import pyttsx3

pyttsx3.speak('I believe you are finding python interesting')