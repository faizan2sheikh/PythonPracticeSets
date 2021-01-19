n=int(input("Enter an integer: "))
sum=0
for i in range(1,n+1):
    if i<n:print('9'*i,end=' ')
    else:print('9'*i)
    sum+=int('9'*i)
print("The sum is: ",sum)    
    
    
