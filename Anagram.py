s = input()
str = input()
temp = sorted(s)
temp1 = sorted(str)

if(temp == temp1):
    print('Anagram')
else:
    print('Not Anagram')