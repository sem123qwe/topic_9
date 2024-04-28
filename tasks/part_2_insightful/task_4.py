user_input: str = input().lower().split()

# TODO: Используйте встроенные методы для решения этой задачи
camelCase: str= "camel"
PascalCase: str = "Pascal"
snake_case: str = "snake_"

clean_line = ""

for i in user_input:
    clean_line += i.capitalize()
    


line: str = "_".join(user_input)
print(camelCase + clean_line)
print(PascalCase + clean_line)
print(snake_case + line)

