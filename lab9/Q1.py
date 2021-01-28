def add(a,b):
    return print(a+b)
def subtract(a,b):
    return print(a-b)
def multiply(a,b):
    return print(a*b)
def divide(a,b):
    return print(a/b)
print('''
    Enter operation you want to perform:
    1.Addition
    2.Subtraction
    3.Multiply
    4.Divide
''')
l=int(input())
v1=int(input('Enter first operand: '))
v2=int(input('Enter second operand: '))
if l==1:add(v1,v2)
elif l==2:subtract(v1,v2)
elif l==3:multiply(v1,v2)
elif l==4:divide(v1,v2)