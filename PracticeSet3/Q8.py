##a. 
a = 0
while a < 100:
        print('*')
        a += 1
## 100

##b.
a = 0
while a < 100:
    b = 0
    while b < 55:
        print('*')
        b += 1
a += 1
## 5500

##c.
a = 0
while a < 100:
    if a % 5 == 0:
        print('*')
    a += 1
#Ans 20

##d.
a = 0
while a > 100:
    print('*')
    a += 1
# none

##e.
a = 0
while a < 100:
    b = 0
    while b < 100:
        c = 0
        while c < 100:
            print('*', end='')
            c += 1
        b += 1
    a += 1
#Ans 100^3 times

##f.
a = 0
while a < 100:
    print('*')
#Infinite times

##g.
a = 0
while a < 100:
    b = 0
    while b < 40:
        if (a+b)%2==0:
            print('*')
        b += 1
    a += 1
#Ans 2000times