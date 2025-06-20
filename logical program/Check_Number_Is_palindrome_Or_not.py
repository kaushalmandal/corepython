n=int(input('Enter the number from user'))
rem=0
sum=0
temp=n
while n>0:
    rem=n%10
    sum=sum*10+rem
    n=n//10
if temp==sum:
    print('number is palindrome')
else:
    print('number is not palindrome')