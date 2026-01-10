# 1. Runtime error 
# 2.  compile type error
# Try, Except, Else and Finally block are used in handling errors in python

var = ['tope', 'alabi', 'shola']
# try:
#     print(var[1])
#     print(x)
# except IndexError as i:
#     print(f'Error: {i}')
# except NameError as n:
#     print(f'Error: {n}')
# except Exception as e:
#     print(f'Error: {e}')



# print('I am here')


def add():
    try:
        val1 = float(input('Value 1: '))
        val2 = float(input('Value 2: '))
        res = val1 / val2
    
    except ZeroDivisionError as z:
        raise ValueError(z) 
    
    except Exception as e:
        print('Error:', e)
    
    else:
        print(res)
    
    finally: 
        print('Bye for now!') 
add()

