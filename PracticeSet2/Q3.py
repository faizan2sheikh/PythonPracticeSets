# i, j, and k are numbers 
i=int(input("Enter value for i: "))
j=int(input("Enter value for j: "))
k=int(input("Enter value for k: "))
if i < j:
    if j < k:
        i = j
    else:
       j = k
else:
    if j > k:
       j = i    
    else:           
        i = k
print("i =", i, " j =", j, " k =", k)

# ANSWERS
#a.i = 5  j = 5  k = 7
#b.i = 3  j = 5  k = 5
#c.i = 7  j = 3  k = 7
#d.i = 5  j = 3  k = 3
#e.i = 5  j = 3  k = 5
#f.i = 7  j = 7  k = 3