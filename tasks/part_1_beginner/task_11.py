user_line = input("")
charg_symbls = "+-."
if charg_symbls in user_line:
    second_line = user_line.isnumeric() != True
    print(second_line)
else:
    print(user_line.isnumeric())
