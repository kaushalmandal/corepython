s=input('Enter random character from string')
count=0
specChar=''
for x in s:
    if x.isalpha():
        pass
    elif x.isnumeric():
        pass
    else:
        specChar=specChar+x
        count=count+1
print('special character is :',specChar)
print('special character count is :',count)