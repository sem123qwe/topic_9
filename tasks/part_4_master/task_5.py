PascalCase = input()
snake_case = ''

for i in range(len(PascalCase)):
    letter = PascalCase[i]
    if i == 0 or i == len(PascalCase) or letter in '0987654321':
        snake_case += letter.lower()
    elif letter == letter.capitalize():
        snake_case += '_' + letter.lower()
    elif letter == letter.lower():
        snake_case += letter

print(snake_case) 