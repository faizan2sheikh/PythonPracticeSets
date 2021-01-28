f=open('Q2.txt')
x=f.read()
x=x.split(' ')
for i in x:
    if i!=x[-1]:print(i,end=',')
    else:print(i)