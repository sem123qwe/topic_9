user_input: str = input()

count: int = 0
i: int = 0
is_word: bool = False
size_line = len(user_input)
while i < size_line:
    if user_input[i] == " ":
        is_word = False
    # elif is_word == False:
    elif not is_word:
        count += 1
        is_word = True

    i += 1
print(count)
