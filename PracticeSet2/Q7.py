x=input("Enter a character: ")
if len(x)==1:
    if x.isalpha():
        print("Its an alphabet")
    elif x.isdigit():
        print("Its a digit")
    elif not x.isalnum():
        print("Its a special character")
else:
    print("Only one character is allowed!")
