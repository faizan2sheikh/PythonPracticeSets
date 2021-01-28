#str1=input("Enter string 1: ")
#str2=input("Enter string 2: ")
#str1=''.join(set(str1))
#str2=''.join(set(str2))
#print(str1)
#for i in str1:
#    if i in str2:
#        print("Common initials are: ",i)
#        str1=str1.replace(i,'')
#for i in str1:       
#    if i not in str2:
#        print("Uncommon initials are: ",i)
#        str1=str1.replace(i,'')
str1=input("Enter string 1: ")
str2=input("Enter string 2: ")
for i in str1:
    if i in str2:print('Common Character:',i)   
    else:print('Uncommon Character:',i)
