
import mysql.connector as sql




# mycursor.execute("CREATE DATABASE todo_app")
# mycursor.execute("""
#     CREATE TABLE todo_table (
#         id INT PRIMARY KEY AUTO_INCREMENT,
#         item VARCHAR(50),
#         description TEXT,
#         status BOOL DEFAULT FALSE,
#         created_at DATETIME DEFAULT CURRENT_TIMESTAMP
#     )         
# """)

class Config:
    def __init__(self):
        self.conn = sql.connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'root',
            password = 'password',
            database = "todo_app"
        )
        self.mycursor = self.conn.cursor()
        self.conn.autocommit = True
        
    
    def create(self, item, description):
        if not item or not description:
            return "Fill in all fields"

        # Insert into the database
        query = "INSERT INTO todo_table(item, description) VALUES(%s, %s)"
        values = (item, description)
        self.mycursor.execute(query, values)
        return "Todo created 🥳"
    
    def read(self):
        self.mycursor.execute("SELECT * FROM todo_table")
        details = self.mycursor.fetchall()
        return details
    
    def update(self, id):
        pass
    
    def delete(self, id):
        pass
    
    def updateStatus(self, id):
        pass
        
    