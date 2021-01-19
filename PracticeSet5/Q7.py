from random import randrange
def fun1(n):
    result = 0
    while n:
        result += n
        n -= 1
    return result
def fun2(stars):
    for i in range(stars + 1):
        print(end="*")
    print()
def fun3(x, y):
    return 2*x*x + 3*y
def fun4(n):
    return 10 <= n <= 20
def fun5(a, b, c):
    return randrange(0, 2)

#1.
print(fun1(5))
#2.
#print(fun1())
#3.
#print(fun1(5, 2))
#4.
print(fun2(5))
#5.
fun2(5)
#6. 
fun2(0)
#7. 
fun2(-2)
#8. 
print(fun3(5, 2))
#9. 
print(fun3(5.0, 2.0))
#10. 
#print(fun3('A', 'B'))
#11. 
#print(fun3(5.0))
#12. 
#print(fun3(5.0, 0.5, 1.2))
#13. 
print(fun4(15))
#14.
print(fun4(5))
#15.
print(fun4(5000))
#16.
#print(fun5())
#17. 
#print(fun5(4))
#18. 
print(fun3(fun1(3), 3))
#19. 
print(fun3(3, fun1(3)))
#20. 
print(fun1(fun1(fun1(3))))