n=int(input("Enter an integer: "))
fact=n
if n>0:
    for i in range(1,n):
        fact*=i
    print(n,"!=",fact)
elif n==0:
    print("0!==1")
            
