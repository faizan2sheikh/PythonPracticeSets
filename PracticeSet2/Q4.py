val = int(input())
if val < 10:
    if val != 5:
       print("wow ", end='')
    else:
       val += 1 
else:
    if val == 17:
      val += 10
    else:
       print("whoa ", end='')
print(val)

# Answers
#a. wow 3
#b. whoa 21
#c. 6
#d. 27
#e. wow -5