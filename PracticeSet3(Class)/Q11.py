while True:
    print("Enter negative number to exit")
    BS=float(input("Enter basic salary: "))
    if BS<0:break
    if BS<=10000:
        HRA=0.2*BS
        DA=0.8*BS
        DD=0.02*BS
    if BS<=20000:
        HRA=0.25*BS
        DA=0.9*BS
        DD=0.04*BS
    if BS>20000:
        HRA=0.3*BS
        DA=0.95*BS
        DD=0.1*BS
    GS=BS+HRA+DA
    NS=GS-DD
    print("The Gross Salary is: ",GS)
    print("The Net Salary is: ",NS)
