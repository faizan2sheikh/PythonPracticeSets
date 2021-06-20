class BankAccount:
    __balancee=0
    def withdraw(self):
        amount=input('Enter the amount you wanna withdraw: ')
        self.__balancee-=int(amount)
    def deposit(self):
        depositt=input('Enter the amount you wanna deposit: ')
        self.__balancee+=int(depositt)
    def balance(self):
        return self.__balancee

b1=BankAccount()
b1.deposit()
b1.withdraw()
print(b1.balance())