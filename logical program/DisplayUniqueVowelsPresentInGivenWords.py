s=input('Enter some string from user')
vowels=['a','e','i','o','u']
found=[]
for x in s:
    if x in vowels:
        if x not in found:
            found.append(x)
print(found)
