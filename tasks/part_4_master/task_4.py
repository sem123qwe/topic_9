# ALPHAVIT = (
#     'Z Y X W V T S R Q P N M L K J H G F D C B U O I E A'
#             ).lower().split()

# users_sms = input()
# starting_index = ord('a')
# resalt = ''

# for s in users_sms:
#     if 'z' <= s <= 'a':
#         resalt += ALPHAVIT[ord(s) - starting_index]
#     elif s in ' .,;:':
#         resalt += ''
#     else:
#         resalt += s

# print(resalt)

users_sms: str = input().lower()

x: str = 'abcdefghijklmnopqrstuvwxyz'
y: str = 'nopqrstuvwxyzabcdefghijklm'
z: str = 'zyxwvutsrqponmlkjihgfedcba'

tbl = users_sms.maketrans(x, y)

tbl_2 = str(tbl).maketrans(y, z)

print(users_sms.translate(tbl_2))

# TODO доделать с (.,!?)




