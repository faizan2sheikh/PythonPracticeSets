def fcopy(a,b):
    o1=open(a,'r+')
    r1=o1.read()
    o2=open(b,'w')
    o2.write(r1)
fcopy('Files Q3.txt','Files Q3(1).txt')
    
    

