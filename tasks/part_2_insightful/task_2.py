user_line = input()
correct_line = ""
b = " "

i = 0
laught = len(user_line)
is_word = False
while i < laught:
    if user_line[i] == "*":
        correct_line += "\n"
    else:
        correct_line += user_line[i]
    i += 1
print(correct_line, )
# TODO (чтобы каждое слово начиналос в верхнем регистре)
