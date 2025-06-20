l=eval(input('Enter list from user'))
min=l[0]
for x in l:
    if x<min:
        min=x
print('minimum value in list is :',min)