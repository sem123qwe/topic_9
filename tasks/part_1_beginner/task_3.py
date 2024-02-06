user_input: str = input()

is_printed: bool = False
out_line: str = ""
for char in user_input:
    # if is_printed == True or char != " ":
    if is_printed or char != " ":
        out_line += char
        print(out_line)
        is_printed = True
