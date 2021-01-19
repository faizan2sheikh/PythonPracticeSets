print("Enter any negative value to terminate: ")
a=float(input("Enter non negative floating point values: "))
min=a
max=a
sum=a
count=1
while True:
    n=float(input('Enter float: '))
    if n>0:
        sum+=n
        if n>max:max=n
        if n<min:min=n
        count+=1
    else:break
print('max is',max)
print('min is',min)
print('average is',sum/count)    
print('sum is',sum)
