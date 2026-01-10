
from my_modules.todoConfig import Config
import time

class MyTodo(Config):
    __app_name = None
    
    def __init__(self, app_name):
        self.__app_name = app_name
        super().__init__()
        
        print(f'Welcome to {self.__app_name}')
        
    def home(self):
        print("""
            1. Add Todo
            2. Edit Todo  
            3. Delete Todo
            4. Mark as completed
            5. View Todo
            #. Exit           
        """)
        
        choice = input("Choice: ")
        if choice == '1':
            self.add_todo()
        elif choice == '5':
            self.viewTodo()
    
    
    def add_todo(self):
        item = input('Todo Item: ').strip().capitalize()
        desc = input('Description: ').strip().capitalize()
        result = self.create(item, desc)
        print('Processing...')
        time.sleep(1)
        print(result)
        self.home()
        
    def viewTodo(self):
        todos = self.read()
        # print(todos)
        for x , todo in enumerate(todos, 1):
            print(f'{x}.  ID-{todo[0]} - {todo[1]} - {todo[2]} - {todo[4]}')
            
        self.home()
        
app = MyTodo('Python Todo')
app.home()
    