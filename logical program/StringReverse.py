words=input('Enter some string from user')
i=len(words)-1
target=''
while i>=0:
    target=target+words[i]
    i=i-1
print(target)
