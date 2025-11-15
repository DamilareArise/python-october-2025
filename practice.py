# Dictionary
# For loop
# while loop
# function
# A Todo app


garage = ['Hyundai', 'Tesla', 'Benz']

car = {
    'brand': 'Benz',
    'model': 'GLC 330',
    'color': 'white',
    'year': '2019',
    # 'owner': {
    #     'fullname': 'Owolabi Owonikoko',
    #     'age': 12,
    #     'address': {
    #         'city': 'Osogbo',
    #         'state': 'Osun',
    #         'country': 'Nigeria'
    #     }
    # }
}
# print(type(car))

# print(car['model'])
# print(f'This is a {car['brand']} {car['model']} {car["year"]} {car['color']}')
# print(car['owner']['fullname'])

car['model'] = 'GLE 350'
# print(car)

# print(car['owner']['address'].keys())
# print(car.values())
# print(car.items())
# print(car.get('Color', 'Not a valid key'))
# car.update({'color': 'Black', 'sold':True, 'brand': (car['brand'], 'Toyota') })
# car.pop('brand')
# car.popitem()
# print(car)

# for i in 'Pelumi':
#     print(f'letter - {i}')
    
# for car in garage:
#     print(car)

# for i in range(10):
#     print(i)

# for key in car.keys():
#     print(key)

# for val in car.values():
#     print(val)

# for key, item in car.items():
#     print(key, item)

# for i in range(1, 6):
#     print(i, 'Times table')
#     for x in range(1, 6):
#         print(f'{i} x {x} = {i*x}')

# for i in range(0, 10, 2):
#     print(i)



# x = 10
# while x > 0:
#     print(x)
#     x-=1


# x = 0
# while x < 10:
#     print(x)
#     x += 1
# else:
#     print('E don finsh oo')


# x = 0
# while x < 10:
#     print(x)
#     if x == 4:
#         break
#     x += 1
    

# ticket = 10
# while ticket > 0:
#     age = int(input('age: '))
#     if age < 18:
#         print('you are too young go watch spongebob')
#         continue
    
#     ticket -= 1
#     print('Take your ticket. remaining', ticket)
       
       
# while True:
#     print('yeye!') 
#     user = input('Enter 1 to exit: ')
#     if user == '1':
#         break
        
        
        
# [
#     {"todo": 'Eating', 'completed': False},
#     {'todo': 'Code', 'completed': True}   
# ]


# function
# A Todo app
# OOP



database = []
def mytodo():
    while True:
        print('''
        Welcome to myTodo      
            1. Add Todo
            2. View 
            3. Delete
            4. Edit
            5. Clear all
            6. Mark as completed
            #. exit
        ''')
        
        user = input('Choice: ')
        if user == '1':
            todo = input('Your Todo: ')
            if todo == '':
                print('Kindly input a todo.')
                continue
        
            todo_dict = {
                'todo': todo,
                'completed': False
            }
            database.append(todo_dict)
            print('Todo added successful')
            
        elif user == '2':
            if not database:
                print('No todo list')
                continue
            for num, data in enumerate(database, 1):
                print(f'{num}. {data['todo']} - {'(Completed)' if data['completed'] else '(Pending)' }')
                
        elif user == '3':
            todo_no = int(input('Delete todo number? '))
            
            if not database:
                print('No todo list')
                continue
            
            elif todo_no > len(database) or todo_no < 1:
                print('Invalid choice')
                continue
            
            deleted = database.pop(todo_no-1)
            print(f'{deleted['todo']} deleted successfully')
                
            
        elif user == '#':
            print('Goodbye!')
            break
        
        else:
            print('Invalid choice')
 
# mytodo()
# true statement: True, 1, 'jajbaj', ['jakna']
# false statement: False, 0, '', []



def greet():
    print('Hello..!')
    
# greet()

def greetName(name, course, time='12pm'):
    print(f'Hello {name}, Welcome to {course} class. class starts by {time}')
    
    
# greetName('Pelumi', 'Data Analysis', '10am')

# return statement

def greet():
    return 'Hello'

# res = greet()
# print(res)



# Local and Global variable

balance = 0 # global

def deposit():
    global balance
    
    amount = float(input('Amount: '))
    balance += amount
    print(f'${amount} deposited successful. Your balance is ${balance} ')
    dashboard()
    
def withdraw():
    global balance
    
    amount = float(input('Amount: '))
    balance -= amount
    print(f'${amount} deposited successful. Your balance is ${balance} ')
    dashboard()
    
def check_balance():
    # return balance
    print(f'Your account balance is ${balance}')
    dashboard()
    
def dashboard():
    print('''
        Welcome to myBank
        1. Deposit
        2. Withdraw
        3. Check balance
        #. Exit  
    ''')
    user = input('choice: ')
    if user == '1':
        deposit()
    elif user == '2':
        withdraw()
    elif user == '3':
        check_balance()
    elif user == '#':
        exit()
    else:
        print('Invalid choice')
        dashboard() #recurssive
    
# dashboard()

# anonymous function

# def add():
#     return 5
        
# def add(a):
#     return 5 + a        
        
# add = lambda : 5

# add = lambda a: 5 + a

# print(add(10))


# documentation

def add(a:int | float, b:int | float = 10) -> float:
    '''
    This function adds up two values
    '''
    return a + b

# add()
    
    

# OOP -> Object Oriented Programming
# class -> Blueprint of the object
# self -> reference to the class

# pillars of OOP.
# 1. Inheritance
# 2. Encapsulation


name = list()
# print(type(name))
# name.


class Human:
    nameA = None
    
    def __init__(self, name):
        self.nameA = name
    
    def talk(self, adj):
        print(f'{self.nameA} is talking {adj}')
        
    
    def changeNameA(self, new):
        self.nameA = new
    

pelumi = Human('Ojo')

# pelumi.talk('Very loudly')
# print(pelumi.name)
# print(type(pelumi))

# pelumi.changeNameA('Pelums')
# print(pelumi.nameA)
pelumi.talk('Softly')



# mrD = Human()

# print(type(mrD))
# mrD.talk('Very calmly')
# mrD.name = 'Mr D'
# print(mrD.name)