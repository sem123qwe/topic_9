user_input = input()
digits = "0987654321"

i = 0
while i < len(user_input):
    if user_input[i] in digits:
        print(user_input[i], end="₽ ")
    i += 1
