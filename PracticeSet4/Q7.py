lst=[3,-3,5,2,-1,2]
sum=0
pstv=[]
if len(lst)>0:
    for i in lst:
        if i>0:
            sum+=i
            pstv.append(i)
    print(sum)
else:
    print('zero')

