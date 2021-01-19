'''The function censor takes the name of a file (a string) as input. The function should open the file, read it, and then
write it into file censored.txt with this modification: Every occurrence of a four-letter word in the file should be
replaced with string 'xxxx'. Note that this function produces no output, but it does create file censored.txt in the
current folder.'''
def censor(a,b):
    f1=open(a)
    f2=open(b,'w')
    text=f1.read()
    text=text.split(' ')
    for i in text:
        if len(i)==4:
            f2.write('xxxx'+' ')
        else:
            f2.write(i+' ')
censor('Q2.txt','censored.txt')

    