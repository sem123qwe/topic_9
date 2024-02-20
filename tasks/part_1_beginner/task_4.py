user_input: str = input()
digits: str = "0987654321"

length: int = len(user_input)
i: int = 0
while i < length:
    if user_input[i] in digits:
        print(user_input[i], end="₽ ")
    i += 1
