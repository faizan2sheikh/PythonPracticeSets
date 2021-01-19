lst=[3,5,4,-1,0]
count=0
pstv=[]
if len(lst)>0:
    for i in lst:
        if i%2==0:
            count+=1
            pstv.append(i)
    print('There are only',count,'even numbers!')
else:
    print('zero')