def avg(b):
    for i in b:
        sum=0
        count=0
        for j in i:
            sum+=j
            count+=1
        print(sum/count)
avg([[95, 92, 86, 87], [66, 54], [89, 72, 100], [33, 0, 0]])
