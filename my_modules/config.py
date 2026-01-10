class BankConfig:
    name = None
    __balance = 0
    
    def __init__(self, bank_name):
        self.name = bank_name
        
    def perform_deposit(self, amount: float):
        if amount <= 0:
            return {
                'status': False,
                'message': 'Invalid amount'
            }
            
        else:
            self.__balance += amount
            return {
                'status': True,
                'message': f'${amount} deposited successfully. Your balance is ${self.__balance}'
            }
            
    def perform_withdraw(self, amount: float):
        if amount <= 0:
            return {
                'status': False,
                'message': 'Invalid amount'
            }
            
        else:
            self.__balance -= amount
            return {
                'status': True,
                'message': f'${amount} withdrawn successfully. Your balance is {self.__balance}'
            }
            
    def get_balance(self):
        return self.__balance
    
    

class TodoConfig:
    pass