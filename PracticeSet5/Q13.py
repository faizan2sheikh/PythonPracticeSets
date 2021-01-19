def points(x1,y1,x2,y2):
    if x1!=x2:
        print("The slope of line is",(y2-y1)/(x2-x1))
    else:print("The slope is infinity")
    print("The distance between points is",((x2-x1)**2+(y2-y1)**2)**.5)

x1=int(input("Enter point x1: "))
x2=int(input("Enter point x2: "))
y1=int(input("Enter point y1: "))
y2=int(input("Enter point y2: "))
points(x1,y1,x2,y2)