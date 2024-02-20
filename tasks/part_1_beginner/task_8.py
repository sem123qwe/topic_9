sentence: str = input()
unic_code: list = []

for num in sentence:
    code = ord(num)
    unic_code.append(code)

max_char_code: int = max(unic_code)
print(max_char_code)
print(chr(max_char_code))


# -------------------- Option 2

sentence: str = input()

max_code: int = -1
for char in sentence:
    char_code: int = ord(char)
    if char_code > max_code:
        max_code = char_code

print(max_code, chr(max_code), sep='\n')
