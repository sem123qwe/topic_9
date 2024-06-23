LOWERCASE_START_ASCII_CODE: int = 97
LOWERCASE_END_ASCII_CODE: int = 122
ENGLISH_ALPHABET_COUNT: int = 26
ROT_13: int = 13

line: str = input().lower()
result: str = ''
for char in line:
    # if char == ' ':
    if char.isspace():
        result += char
    elif char.isalpha():
        # curr_code: int = ord(char)
        # make = (curr_code - LOWERCASE_START_ASCII_CODE) + ROT_13
        # make = make % ENGLISH_ALPHABET_COUNT
        # res_code = LOWERCASE_END_ASCII_CODE - make
        # print(chr(res_code))

        result += chr(
            LOWERCASE_END_ASCII_CODE
            - ((ord(char) - LOWERCASE_START_ASCII_CODE) + ROT_13)
            % ENGLISH_ALPHABET_COUNT
        )

print(result)
