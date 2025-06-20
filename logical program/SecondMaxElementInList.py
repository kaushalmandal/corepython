l=eval(input('Enter list from user'))
max=l[0]
for x in l:
    if x>max:
        max=x
print('max element in list is :',max)
l.remove(max)
secmax=l[0]
for x in l:
    if x>secmax:
        secmax=x
print('second max element in list is :',secmax)