def crypto(a):
    f=open(a)
    text=f.read()
    text=text.replace('secret','xxxxxx')
    print(text)
crypto('crypto.txt')