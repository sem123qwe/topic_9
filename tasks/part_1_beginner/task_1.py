user_input: str = input()

right_line: str = ""

calculate: int = len(user_input)
i = 0
while i < calculate:
    pass
print(right_line)


# ------------------- Example

toys: str = 'yytreeevvbbd'
unique_toys: str = ''

i: int = 0
length: int = len(toys)
while i < length:
    if toys[i] not in unique_toys:
        unique_toys += toys[i]

    i += 1
