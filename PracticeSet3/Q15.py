sum=0
count=0
for i in range(3):
    a=float(input("Enter a number: "))
    sum+=a
    count+=1
avg=sum/count
b=float(input("Enter a number: "))
if avg==b:
    print("EQUAL")
else:print("NOT EQUAL")
    
