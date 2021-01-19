a=int(input("Enter an integer: "))
b=int(input("Enter an integer: "))
c=int(input("Enter an integer: "))
d=int(input("Enter an integer: "))
e=int(input("Enter an integer: "))
max=a
min=a
if a>b and a>c and a>d and a>e:max=a
if b>a and b>c and b>d and b>e:max=b
if c>a and c>b and c>d and c>e:max=c
if d>a and d>b and d>c and d>e:max=d
if e>a and e>b and e>c and e>d:max=e
if a<b and a<c and a<d and a<e:min=a
if b<a and b<c and b<d and b<e:min=b
if c<a and c<b and c<d and c<e:min=c
if d<a and d<b and d<c and d<e:min=d
if e<a and e<b and e<c and e<d:min=e
print("The maximum value is: ",max)
print("The minimum value is: ",min)


    
