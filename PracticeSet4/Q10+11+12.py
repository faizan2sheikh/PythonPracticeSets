def PrintMat(matrix,x):
    ''' takes matrix as list and print it in matrix format'''
    print(x,'matrix is:')
    for lst in matrix:
        print('|',end='\t')
        for element in lst:
            print(element,end="\t")
        print('|')
    return('~'*98)#Just customization


def InputMat(x,r):
    '''Takes matrix input of any order given by user'''
    matrix=[]
    for row in range(1,r+1):
        print('Enter values for matrix',x,' row',str(row),'separated by commas:',end=' ')
        row_1=input()
        matrix.append(row_1.split(","))
    return matrix

r1=int(input('Enter No. of rows for first matrix: '))
c1=int(input('Enter No. of columns for first matrix: '))
mat_1=InputMat(1,r1) #Taking matrix 1 input
print()

r2=int(input('Enter No. of rows for second matrix: '))
c2=int(input('Enter No. of columns for second matrix: '))  
mat_2=InputMat(2,r2) #Taking matrix 2 input

print(PrintMat(mat_1,'First'))#printing matrix 1 for user's ease
print(PrintMat(mat_2,'Second'))#printing matrix 2 for user's ease

print('''                         What operation do you want to perform?
                        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                    -----------------------    
                                    |    1=addition       |
                                    |    2=subtraction    |
                                    |    3=multiplication |
                                    |    4=exit           |
                                    -----------------------''')##Menu For Operations
oper=int(input('I want to do: '))##User's choice


while True:
    if oper==4:break ##If user choose 4 then program exits
    if oper==1: #addition
        if r1==r2 and c1==c2:  #checks the criteria for addition operation
            print('The result of addition of these matrices is: ')
            for e1 in range(0,r1):
                print('|',end='\t')
                for e2 in range(0,c1):             
                    print(int(mat_1[e1][e2]) + int(mat_2[e1][e2]),end='\t')
                print('|')
        else:
            print("Matrices are not suitable for Addition!")
            break

    if oper==2: #Subtraction
        if r1==r2 and c1==c2:   #checks the criteria for subtraction operation
            print('The result of subtraction of these matrices is: ')
            for e1 in range(0,r1):
                print('|',end='\t')
                for e2 in range(0,c1):             
                    print(int(mat_1[e1][e2]) - int(mat_2[e1][e2]),end='\t')
                print('|')
        else:
            print("Matrices are not suitable for Subtraction!")
            break

    if oper==3: #Multiplication
        if c1==r2:  #checks the criteria for multiplication operation
            print('The result of multiplication of these matrices is: ')
            for l in range(len(mat_1)):
                print('|',end='\t')
                for m in range(len(mat_2[0])):
                    b=0           
                    for n in range(len(mat_2)):            
                        a=(int(mat_1[l][n]) * int(mat_2[n][m]))
                        b+=a
                    print(b,end='\t')
                print('|')
        else:
            print("Matrices are not suitable for Multiplication!")
            break
    print()
    print('''                         What operation do you want to perform?
                        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                    -----------------------    
                                    |    1=addition       |
                                    |    2=subtraction    |
                                    |    3=multiplication |
                                    |    4=exit           |
                                    -----------------------''')
    oper=int(input('I want to do: '))#Reprinting of menu for user's choice


print('ThankYou! You were using Matrix Calculator made by Faizan!')## Exit with greetings!
