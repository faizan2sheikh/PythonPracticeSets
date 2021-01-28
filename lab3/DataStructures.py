x = (input("Enter your password: "))
num = ('0'in x)or('1'in x)or('2'in x)or('3'in x)or('4'in x)or('5'in x)or('6'in x)or('7'in x)or('8'in x)or('9'in x)
special = (')'in x)or('!'in x)or('@'in x)or('#'in x)or('$'in x)or('%'in x)or('^'in x)or('&'in x)or('*'in x)or('('in x)
if 7<=len(x)<=15 and num and special:
    print("Your password is correct!")
else:
    print("Your password must contain 7-15 characters, at least a numeric value and a special character!")
