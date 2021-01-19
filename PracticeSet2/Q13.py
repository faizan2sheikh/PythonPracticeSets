bs=float(input("Enter basic salary: "))
if bs<=10000:
    hra=0.2*bs
    da=0.8*bs
    dd=.02*bs
elif bs<=20000:
    hra=0.25*bs
    da=0.9*bs
    dd=0.04*bs
elif bs>20000:
    hra=0.3*bs
    da=0.95*bs
    dd=.1*bs
gs=bs+hra+da
ns=gs-dd
print("The Gross Salary is: ",gs)
print("The Net Salaray is: ",ns)
    
