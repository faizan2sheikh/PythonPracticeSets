pattern=[]
for i in range(1,4):
    print('Enter state',i,'for row',str(i),'separated by commas:',end=' ')
    i=input()
    pattern.append(i.split(","))


for row in pattern:
    print('|',end='\t')
    for state in row:
        print(state,end='\t')
    print('|')

if (pattern[0][0] == pattern[0][1] == pattern[0][2]) and (pattern[0][0]=='O'or'X'):print(pattern[0][0])
elif (pattern[1][0] == pattern[1][1] == pattern[1][2]) and (pattern[1][0]=='O'or'X'):print(pattern[1][0])
elif (pattern[2][0] == pattern[2][1] == pattern[2][2]) and (pattern[2][0]=='O'or'X'):print(pattern[2][0])
elif (pattern[0][0] == pattern[1][0] == pattern[2][0]) and (pattern[0][0]=='O'or'X'):print(pattern[0][0])
elif (pattern[0][1] == pattern[1][1] == pattern[2][1]) and (pattern[0][1]=='O'or'X'):print(pattern[0][1])
elif (pattern[0][2] == pattern[1][2] == pattern[2][2]) and (pattern[0][2]=='O'or'X'):print(pattern[0][2])
elif (pattern[0][0] == pattern[1][1] == pattern[2][2]) and (pattern[0][0]=='O'or'X'):print(pattern[0][0])
elif (pattern[0][2] == pattern[1][1] == pattern[2][0]) and (pattern[0][2]=='O'or'X'):print(pattern[0][2])
else:print(' ')






