x=input("Enter a character: ")
if len(x)==1:
    if x.isalpha():
        if x.isupper():
            print("Its an uppercase alphabet")
        else:
            print("Its a lowercase alphabet")
    else:
        print("Its not an alphabet")
else:
    print("Only one character is allowed!")
