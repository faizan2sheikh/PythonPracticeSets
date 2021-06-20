class BankAccount:
    balancee=0
    def withdraw(self):
        amount=input('Enter the amount you wanna withdraw: ')
        self.balancee-=int(amount)
    def deposit(self):
        depositt=input('Enter the amount you wanna deposit: ')
        self.balancee+=int(depositt)
    def balance(self):
        return self.balancee

b1=BankAccount()
b1.deposit()
b1.withdraw()
print(b1.balancee)