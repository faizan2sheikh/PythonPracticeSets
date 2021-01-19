n=float(input("Enter units consumed: "))
if n<=50:
    print("The electricity bill is: ",n*.5,"Rs")
elif n<=150:
    a=((n-50)*.75)+(50*.5)
    print("The electricity bill is: ",a,"Rs")
elif n<=250:
    a=(100*.75)+(50*.5)+((n-150)*1.2)
    print("The electricity bill is: ",a,"Rs")
elif n>250:
    a=(100*.75)+(50*.5)+(100*1.2)+((n-250)*1.5)
    print("The electricity bill is: ",a,"Rs")
    
    
