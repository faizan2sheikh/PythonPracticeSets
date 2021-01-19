def distribution(a):
    f=open(a)
    text=f.read()
    text=text.split(' ')
    countA=0
    countA1=0
    countB2=0
    countB=0
    countB1=0
    countC=0
    countC1=0
    countF=0
    for i in text:
        if i=="A":countA+=1
        if i=="A-":countA1+=1
        if i=="B":countB+=1
        if i=="B+":countB2+=1
        if i=="B-":countB1+=1
        if i=="C":countC+=1
        if i=="C-":countC1+=1
        if i=="F":countF+=1
    print(countA,"Students got A")
    print(countA1,"Students got A-")
    print(countB2,"Students got B+")
    print(countB,"Students got B")
    print(countB1,"Students got B-")
    print(countC,"Students got C")
    print(countC1,"Students got C-")
    print(countF,"Students got F")
distribution('Files Q4.txt')
