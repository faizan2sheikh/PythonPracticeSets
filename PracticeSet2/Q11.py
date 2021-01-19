a=float(input("Enter length of side 1: "))
b=float(input("Enter length of side 2: "))
c=float(input("Enter length of side 3: "))
if a==b and a==c:print("The triangle is equilateral")
elif a==b or a==c:print("The traingle is iscosceles")
elif a!=b and a!=c:print("The triangle is scalene")

