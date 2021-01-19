def duplicate(a):
    f=open(a)
    text=f.read()
    text=text.split(' ')
    count=0
    for i in text:
        count=text.count(i)
    if count>1:print("True")
    else:print("False")
duplicate('Q5.txt')
