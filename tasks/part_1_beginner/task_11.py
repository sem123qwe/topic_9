user_line: str = input()

correct_symbls: str = "+-."
digits: str = "0987654321"
is_num: bool = True

count: int = 0
for char in user_line:
    if ((char not in digits)
        and (char not in correct_symbls)
        and char != " "):
        is_num = False
        break
    elif char == ".":
        count += 1

        if count > 1:
            is_num = False
            break

print(is_num)
