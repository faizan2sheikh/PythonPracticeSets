sum=0
max=0
min=1000

for i in range(1,21):
    n=float(input('Enter integer: '))
    sum+=n
    if n>max:
        max=n
    if n<min:
        min=n
print('max is',max)
print('min is',min)
print('average is',sum/i)    
print('sum is',sum)