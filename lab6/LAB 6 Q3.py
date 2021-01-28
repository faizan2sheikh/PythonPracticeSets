gadgets=['Mobile','Laptop',100,'Camera',310.28,'Speakers',27.00,'Television',1000,'Laptop Case','Camera Lens']
numlst=[]
strlst=[]
for i in gadgets:
    if isinstance(i,str):
        strlst.append(i)
    else:numlst.append(i)
print(strlst)
print(numlst)
strlst.sort()
print(strlst)
strlst.reverse()
print(strlst)
numlst.sort()
print(numlst)
numlst.reverse()
print(numlst)
