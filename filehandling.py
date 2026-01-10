# mode
# 1. read only - r
# 2. write only - w
# 3. append - a
# 4. create - x

# try: 
#     file = open(r'C:\python_oct\todo.py', "rt")
#     # print(file.read(5))
#     # print(file.readline())
#     # print(file.readlines()[6])
# except Exception as e:
#     print('Error:', e)
    
# finally:
#     file.close()


# with open('test.txt', 'w') as file:
#     file.write('Welcome to class')
    
# with open('test.txt', 'a') as file:
#     file.write('Welcome to class\n')
    
# with open('test.pdf', 'x') as file:
#     pass

# file = open(r'C:\python_oct\todo.py', "rt")
# print(file.read(5))
# file.close()
# print(file.read(5))

# with open(r"test.txt", "rt", encoding='utf-8') as file:
#     print(file.read())
    
# print(file.read(10))

names = []
heights = []

with open('president_height.csv') as file:
    data = file.readlines()
    data.pop(0)
    # print(data)
    
    for item in data:
       val = item.split(',')
       name = val[1]
       height = int(val[2].strip('\n'))
       names.append(name)
       heights.append(height)
       
       
# print(names)
# print(min(heights))

# print(sum(heights)/len(heights))

# for name, height in zip(names, heights):
#     print(f'{name} has height {height}cm')

# index = 0
# for height in heights:
#     if height == min(heights):
#         print(names[index])
    
#     index += 1

import statistics as stat

mode = stat.mode(heights)
# print(mode)
index = 0
for height in heights:
    if height == mode:
        print(names[index])
    
    index += 1