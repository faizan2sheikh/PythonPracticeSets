def natural_sum(n):
    if n<=1:return n
    else:return n+natural_sum(n-1)
n=int(input('Enter limit:'))
print(natural_sum(n))
