PascalCase = input().strip()
snake_case = ''

for i in range(len(PascalCase)):
    letter = PascalCase[i]
    if i == 0 or i == len(PascalCase) or letter in '0987654321':
        snake_case += letter.lower()
    elif letter == letter.capitalize():
        snake_case += '_' + letter.lower()
    elif letter.islower():
        snake_case += letter

print(snake_case)

# №2
line: str = input().strip()

result: str = line[0].lower()
for char in line[1:]:
    if char.isupper():
        result += '_'
    result += char.lower()

print(result)
