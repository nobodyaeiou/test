char = 'HelloWorld'

for i in range(len(char)):
    andChar = ord(char[i]) & 127
    print(andChar, end="")
print('\n')

for i in range(len(char)):
    orChar = ord(char[i]) | 127
    print(orChar, end="")
print('\n')

for i in range(len(char)):
    xorChar = ord(char[i]) ^ 127
    print(xorChar, end="")
print('\n')
