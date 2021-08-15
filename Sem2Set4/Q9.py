try:
    lst = [0, 0, 0, 0]
    with open('data.txt', 'r') as f:
        count = 0
        for line in f.readlines():
            lst[count] = int(line)
            count += 1
except FileNotFoundError:
    print('file not found')
except ValueError:
    print('int() method cannot convert this data in integer type')