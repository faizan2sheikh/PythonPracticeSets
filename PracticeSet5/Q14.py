def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:count+=1
    return count==2
def check(n):
    return '2' in str(n) or '3' in str(n)
for i in range(1,1000):
    if prime(i) and check(i):
        print(i)
