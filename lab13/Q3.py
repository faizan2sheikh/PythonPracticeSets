f=open('Q3.txt')
l=0
x=f.read()
x=x.split(' ')
for i in x:
    if len(i)>l:
        longest=i
        l=len(i)
print(longest)

