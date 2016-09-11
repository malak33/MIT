str1 = 'exterminate!'
str2 = 'number one - the larch'
str2 = str2.capitalize()
str2.swapcase()

print(str2)
print(str1.index('e'))
print(str2.index('n'))
print(str2.find('n'))
print(str2.find('!'))
print(str1.count('e'))
str1 = str1.replace('e', '*')
print(str1)
str2.replace('one', 'seven')
print(str2)