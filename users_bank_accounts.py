# USER CLASS INSTANTIATED
class User:
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.account = BankAccount(int_rate = 0.02, account_balance = 0)


    def display_user_balance(self):
        
        print(f"User: {self.first_name} {self.last_name}, Balance: {self.account.display_account_info()}")
        return self


    def transfer_money(self, amount, user):
        self.account.account_balance -= amount
        user.account.account_balance += amount
        self.display_user_balance()
        user.display_user_balance()
        return self





# BANK ACCOUNT CLASS INSTANTIATED
class BankAccount:

    accounts = []

    def __init__(self, int_rate, account_balance):
        self.int_rate = int_rate
        self.account_balance = account_balance
        BankAccount.accounts.append(self)


    def deposit(self, amount):
        self.account_balance += amount

        return self


    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.account_balance, amount):
            self.account_balance -= amount
        else:
            print ('Insufficient Funds: Charging $5.00 Fee')
            self.account_balance -= 5

        return self
    
    @staticmethod
    def can_withdraw(account_balance, amount):
        if (account_balance - amount) < 0:
            return False
        else:
            return True


    def display_account_info(self):
        return f"{self.account_balance}"


    def yield_interest(self):
        if BankAccount.can_yield_int(self.account_balance):
            self.account_balance += (self.account_balance * self.int_rate)
        else:
            print('Insufficient Funds')
        return self
    

    @staticmethod 
    def can_yield_int(account_balance):
        if account_balance < 0:
            return False
        else:
            return True


    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()



#Instantiate Users with Bank Accounts
Nick = User ('Nick', 'Chambers', 30)
Bruce = User ('Bruce', 'Wayne', 45)


Nick.account.deposit(300).deposit(500).withdraw(400).yield_interest()
Bruce.account.deposit(2000).deposit(5000).withdraw(1500).withdraw(1000).yield_interest()

Nick.display_user_balance()
Bruce.display_user_balance()

Bruce.transfer_money(500, Nick)





