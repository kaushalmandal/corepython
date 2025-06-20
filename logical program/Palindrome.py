s=input('Enter some string from user')
i=len(s)-1
s1=''
while i>=0:
    s1=s1+s[i]
    i=i-1
if s==s1:
    print('string is palindrome')
else:
    print('string is not palindrome')

