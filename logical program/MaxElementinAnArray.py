l=eval(input('Enter list from user'))
max=l[0]
for x in l:
    if x>max:
        max=x
print('max value in list is :',max)