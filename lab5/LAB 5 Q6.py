while True:
    i=input('Enter Your ID:')
    print('Current Id','*'*len(str(i)))
    print("Main Menu")
    print("*************")
    print("1. Deposit Money")
    print('2. Withdraw Money')
    print('3. Login as Different User')
    print('Enter your choice number: ',end=' ')
    a=input()
    if a=='1':
        print("Your money has been deposited")
        print("Do you want to continue[n/y]")
        b=input()
        if b=='n':break
        if b=='y':continue
    if a=='2':
        print("Your money has been withdrawed")
        print("Do you want to continue[n/y]")
        b=input()
        if b=='n':
            break
        if b=='y':continue
    if a=='3':
        print("Logged in as different user")
        print("Do you want to continue[n/y]")
        b=input()
        if b=='n':break
        if b=='y':continue
        
