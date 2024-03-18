user_line = input()

words = 0
lenght = len(user_line)
is_word = False
i = 0

if user_line == "":
    print(False)

while i < lenght:
    if user_line[i] == " ":
        is_word = False
    elif not is_word:
        words += 1
        is_word = True
    i += 1
print(words)
