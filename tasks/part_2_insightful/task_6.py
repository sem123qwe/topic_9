# TODO: Задачу необходимо решить используя встроенные методы строк
text = input()

counter_num = 0
counter_letter = 0
counter_space = 0
num = 0
laught = len(text)
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