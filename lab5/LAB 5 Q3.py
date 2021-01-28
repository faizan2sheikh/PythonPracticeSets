l=input("Enter your list seperated by comma: ")
l=l.split(',')
lst=[]
for i in l:
    lst.append(int(i))
large=lst[0]
for i in lst:
    if i>large:large=i
print("The largest integer is: ",large)
