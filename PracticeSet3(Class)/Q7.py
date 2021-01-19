n=int(input("Enter an integer: "))
sum=0
for i in range(1,n+1):
    sum+=1/i
    if i<n:print("1/",i,"+",end=' ')
    else:print("1/",i)
print("The sum is: ",sum)
        
