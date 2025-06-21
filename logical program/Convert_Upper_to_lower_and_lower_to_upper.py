s=input('Enter any string from user')
res=''
for x in s:
    if ord(x)>=97 and ord(x)<=122:
        res=res+chr(ord(x)-32)
    elif ord(x)>=65 and ord(x)<=90:
        res=res+chr(ord(x)+32)
    elif ord(x)==32:
        res=res+''
print(res)
