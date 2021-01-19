ph=float(input("Enter marks of physics: "))
ch=float(input("Enter marks of chemistry: "))
ma=float(input("Enter marks of mathematics: "))
bi=float(input("Enter marks of biology: "))
co=float(input("Enter marks of computer: "))
pe=((ph+ch+ma+bi+co)/500)*100
if pe>=90:
    print("The percentage is: ",pe,"%")
    print("GRADE A")
elif pe >=80:
    print("The percentage is: ",pe,"%")
    print("GRADE B")
elif pe>=70:
    print("The percentage is: ",pe,"%")
    print("GRADE C")
elif pe>=60:
    print("The percentage is: ",pe,"%")
    print("GRADE D")
elif pe>=40:
    print("The percentage is: ",pe,"%")
    print("GRADE E")
elif pe<40:
    print("The percentage is: ",pe,"%")
    print("GRADE F")
