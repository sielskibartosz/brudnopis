class DupaBlada(Exception):
    def __init__(self, *args):
        print("dupa")
        super().__init__(*args)

class InsufficientFundsError(Exception):
    def __init__(self, balance: float, amount: float):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Brak środków: saldo {balance}, próba wypłaty {amount}")

class Account:
    def __init__(self, name:str,balance:float=0.0):
        self.name = name
        self.__balance = balance

    def deposit(self, amount:float):
        if amount <0:
            raise DupaBlada("ojoj0")
        else:
            self.__balance += amount

    def withdraw(self,amount:float):
        if amount <0:
            raise ValueError("ojoj1")
        elif amount > self.__balance:
            raise InsufficientFundsError(self.__balance, amount)
        else:
            self.__balance -= amount
    @property
    def balance(self):
        return self.__balance

bartek = Account("Bartek",1000)
print(bartek.balance)

try:
    bartek.withdraw(5000)
except InsufficientFundsError as e:
    print(e)
