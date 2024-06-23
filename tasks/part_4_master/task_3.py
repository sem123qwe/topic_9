IPv4 = int(input())

convert = str(bin(IPv4))[2::]

spicoc = ''

for i in convert:
    if int(i) % 8 == 0:
        spicoc += i    
    elif int(i) % 8 != 0:
        spicoc += i + '.'

print(convert)
print(spicoc)

        





