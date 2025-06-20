s=input('Enter some string from user')
i=0
print('character at even position')
while i<len(s):
    print(s[i],end=' ')
    i=i+2
print('character at odd position')
i=1
while i<len(s):
    print(s[i],end=' ')
    i=i+2
