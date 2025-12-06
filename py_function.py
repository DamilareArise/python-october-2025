# Declaration stage, Definition stage, Invocation Stage

def sayHello(): #declaration stage
    print('Hello.!') #definition stage
    
# sayHello() #invocation stage


def add():
    val1 = float(input('val 1: '))
    val2 = float(input('val 2: '))
    print('Ans: ', val1 + val2)
    
# add()

# Return function

def getUser():
    return 'Aisha'

# print(getUser())
user = getUser()
# print(user)

# Parametized and Non-Parametized function
# name = 'jb'
# name.lower()
# name.split()

def sayHello(name):
    print('Hello', name)

# sayHello(name='Jb')
# sayHello('Dami')

def add(val1, val2):
    print('ans:', val1+val2)
   
   
# val1 = float(input('Val1: ')) 
# val2 = float(input('Val12: ')) 
# add(val1, val2)

def areaOfCircle(r):
    result = 3.142 * (float(r) ** 2)
    return result

# print(areaOfCircle(5))

# radius = float(input('radius: '))
# aoc = areaOfCircle(radius)
# print(aoc)

def addToAOC(radius, value):
    result = value + areaOfCircle(radius)
    return result


# radius = float(input('radius: '))
# val = float(input('value: '))

# res = addToAOC(radius, val)
# print(res)



def getSpeed(time:float, distance: float = 10) -> float | int:
    """
    Formula for calculating speed

    Args:
        time (float): Time in seconds
        distance (int, optional): Distance in meter. Defaults to 10.

    Returns:
        float: speed = distance/time (m/s)
    """
    return float(distance)/float(time)

# res = getSpeed(10, 2)
# print(res)


# global and local variables 

val = 10 # global variable

def add():
    global val1, val
    
    val1 = 20 # local
    res = val1 + val
    print(res)
    
    val -= 5
    
    
def subtract():
    
    res = val1 - val
    print(res)
    
# add()
# subtract()


balance = 0

def home():
    print('''
        1. Deposit
        2. Withdraw
        3. Check balance
        #. exit
    ''')
    choice = input('choice: ')
    if choice == '1':
        deposit()
    elif choice == '2':
        withdraw()
    elif choice == '3':
        checkbalance()
    elif choice == '#':
        print('Goodbye!')
        exit()
    else:
        print('Invalid input')
        home() # recurssive function

def deposit():
    global balance
    amount = float(input('Amount: '))
    balance += amount
    balance = round(balance, 2)
    print('Deposit successful')
    home()
    
def withdraw():
    global balance
    amount = float(input('Amount: '))
    balance -= amount
    balance = round(balance, 2)
    print('Withdrawal successful')
    home()
    
def checkbalance():
    print(f'Balance is #{balance:,}')
    home()
    

home()