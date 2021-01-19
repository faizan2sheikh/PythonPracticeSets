n=int(input("Enter an integer: "))
a=0
b=1
print("0 1",end=' ')
for i in range(n-2):
   c=a+b
   a=b
   b=c
   print(c,end=' ')
