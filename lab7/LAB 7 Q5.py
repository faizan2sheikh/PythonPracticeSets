r=input("Enter list of multiple choice responses seperated by comma: ")
r=r.split(',')
count=1
Q='Q'
d={}
for i in r:
    Q='Q'+str(count)
    d[Q]=i
    count+=1
print(d)
    
