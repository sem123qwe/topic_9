sentence = input("")
unic_code = []

for num in sentence:
    code = ord(num)
    unic_code.append(code)

print(max(unic_code))
print(chr(max(unic_code)))
