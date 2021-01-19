a=input("Enter a sentence: ")
count=0
for i in range(len(a)):
    if a[i] in "aeiou" or a[i] in 'AEIOU': 
        count+=1
print(count)        
    
