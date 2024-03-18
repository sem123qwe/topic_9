user_input: str = input()
right_line: str = ""

calculate: int = len(user_input)
i = 0
while i < calculate:
    if user_input[i] not in right_line:
        right_line += user_input[i]
    i += 1
print(right_line)

# Option 2
user_input: str = input()
right_line: str = ""

for char in user_input:
    if char not in right_line:
        right_line += char

print(right_line)
