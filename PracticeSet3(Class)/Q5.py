n=int(input("Enter an integer: "))
count=0
for i in range(1,n+1):
    if i<n:
        if n%i==0:print(i,end=',')
if i==n:print(i)    
        

  
