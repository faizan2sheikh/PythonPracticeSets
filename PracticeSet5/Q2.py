#Incorrect Program
def proc(x):
    x = 2*x*x
def main():
    num = 10
    proc(num)
    print(num)
main()

#Corrected Program
def proc1(x):
    return 2*x*x
def main1():
    num = 10
    print(proc1(num))
main1()