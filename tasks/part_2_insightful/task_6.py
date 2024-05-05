# TODO: Задачу необходимо решить используя встроенные методы строк
text = input()

counter_num: int = 0
counter_letter: int = 0
counter_space: int = 0
num: int= 0
laught: int = len(text)
while num < laught:
    if text[num].isdigit():
        counter_letter += 1
    elif text[num].isalpha():
        counter_num += 1
    elif text[num] == " ":
        counter_space += 1
    num += 1

print(counter_num)
print(counter_letter)
print(counter_space)

# Option 2
counter_num: int = 0
counter_letter: int = 0
counter_space: int = 0
for char in text:
    if char.isnumeric():
        counter_letter += 1
    elif char.isalpha():
        counter_num += 1
    elif char.isspace():
        counter_space += 1
print(counter_num)
print(counter_letter)
print(counter_space)
