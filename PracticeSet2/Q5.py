x=input("Enter a character: ")
if len(x)==1:
    if x.isalpha():
        print("Its an alphabet")
    else:
        print("Its not an alphabet")
else:
    print("Only one character is allowed!")
