a=int(input("Enter an integer: "))
b=int(input("Enter an integer: "))
c=int(input("Enter an integer: "))
d=int(input("Enter an integer: "))
e=int(input("Enter an integer: "))
count=0
if a==b or a==c or a==d or a==e:count+=1
if b==c or b==d or b==e:count+=1
if c==d or c==e:count+=1
if d==e:count+=1
if count>=1:print("DUPLICATES")
if count==0:print("ALL UNIQUE")

