def sum1(n):
    s = 0
    while n > 0:
        s += 1
        n -= 1
    return s
def sum2():
    global val
    s = 0
    while val > 0:
        s += 1
        val -= 1
    return s
def sum3():
    s = 0
    for i in range(val, 0, -1):
        s += 1
    return s
#def main():
# See each question below for details
#main()  Call main function

#a.
def main1():
    global val
    val = 5
    print(sum1(5))
    print(sum2())
    print(sum3())
main1()

#b.
def main2():
    global val
    val = 5
    print(sum1(5))
    print(sum3())
    print(sum2())
main2()

#c.
def main3():
    global val
    val = 5
    print(sum2())
    print(sum1(5))
    print(sum3())
main3()

#d. sum2
#e. sum1
#f. global , lifetime is until function main
#g. local , inside sum(3) only
#h. lambi nahi , sum1 prints same ,sum2 prints same but makes global val=0 , sum3 prints same

