varA = 1
varB = 3

if type(varA) == str or type(varB) == str:
    print('string involved')
elif int(varA) > int(varB):
    print('bigger')
elif int(varA) == int(varB):
    print('equal')
else:
    int(varA) < int(varB)
    print('smaller')

print()
print('#############')
print('#############')
print('#############')
print()

num = 2
while num < 11:
    print(num)
    num += 2
print('Goodbye!')

print()
print('#############')
print('#############')
print('#############')
print()

for n in range(2,12, 2):
    print(n)
print('Goodbye!')

print()
print('#############')
print('#############')
print('#############')
print()

num = 10
for num in range(5):
    print(num)
print(num)

print()
print('#############')
print('#############')
print('#############')
print()


divisor = 2
for num in range(0, 10, 2):
    print(num/divisor)

print()
print('#############')
print('#############')
print('#############')
print()

for variable in range(20):
    if variable % 4 == 0:
        print(variable, end='\n')
    if variable % 16 == 0:
        print('Foo!', end='\n')

print()
print('#############')
print('#############')
print('#############')
print()

for letter in 'hola':
    print(letter)


print()
print('#############')
print('#############')
print('#############')
print()

count = 0
for letter in 'Snow!':
    print('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    break
print(count)

print()
print('#############')
print('#############')
print('#############')
print()

school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons))

print()
print('#############')
print('#############')
print('#############')
print()

greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter)

print('done')

print()
print('#############')
print('#############')
print('#############')
print()

s = 'azcbobobegghakl'
numVowels = 0

for char in s:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
print('Number of vowels: ' + str(numVowels))

print()
print('#############')
print('#############')
print('#############')
print()

s = 'azcbobobegghakl'
numBob = 0
var = 'bob'

for char in s:
    if char == var:
        numBob += 1
print('Number of times bob occurs is: ' + str(numBob))

print()
print('#############')
print('#############')
print('#############')
print()

#import regex as re
s = 'azcbobobegghakl'
# s = {}
numBob = 0
s2 = 'bob'
#prog = re.compile(s)
# result = prog.match(string)

#re.findall(s2, s)
# match = re.findall(r'(?=(\w\w))', s2)
match = re.findall(r'(?=(\w\w))', s2, overlapped=True)
#s.count('bob')
numBob += 1

print(match)
print('Number of times bob occurs is: ' + str(numBob))\


test = s[0]
best = ''

for n in range(1, len(s)):
 if len(test) > len(best):
     best = test
 if s[n] >= s[n - 1]:
     test = test + s[n]
 else:
     test = s[n]

print("Longest substring in alphabetical order is:", best)

print()
print('#############')
print('#############')
print('#############')
print()

num = 10
print('Hello!')
while num > 1:
    print(num)
    num -= 2

print()
print('#############')
print('#############')
print('#############')
print()

#end = 6
end = 16
n = 0
# start = 1
formula = []
while n < end + 1:
    # for n in range(0, end + 1):
    # print(formula)
    # print()
    # print(sum(formula))
    n += 1
    formula.append(n)
print(sum(formula[:-1]))

print()
print('#############')
print('#############')
print('#############')
print()

n = 0
# start = 1
formula = []
while n < end:  # + 1:
    # for n in range(0, end + 1):
    # print(formula)
    # print()
    # print(sum(formula))
    n += 1
    formula.append(n)
print(sum(formula))

print()
print('#############')
print('#############')
print('#############')
print()

# Here is one of a few ways to solve this problem:
total = 0
current = 1
while current <= end:
    total += current
    current += 1

print(total)

print()
print('#############')
print('#############')
print('#############')
print()

print('Hello!')
for n in reversed(range(2, 12, 2)):
    print(n)

print()
print('#############')
print('#############')
print('#############')
print()

end = 6
total = 0
current = 1
for i in range(0, end):
    current <= end
    total += current
    current += 1

print(total)