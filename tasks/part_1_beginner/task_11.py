user_line: str = input()
correct_symbls: str = "0987654321+-."
count: int = 0


# num = 0
# size_line = len(user_line)
# while num < size_line:
#     if user_line[num] not in correct_symbls or count > 1:
#         print(False)
#         break

#     if "." in user_line[num]:
#         count += 1
#     else:
#         print(user_line[num] in correct_symbls)

#     num += 1

# num = 0
# size_line = len(user_line)
# while num < size_line:
#     if user_line[num] not in correct_symbls or count > 1:
#         print(False)
#         break

#     if "." in user_line[num]:
#         count += 1
#     else:
#         print(user_line[num] in correct_symbls)

#     num += 1

conditions = correct_symbls not in user_line
print(conditions)
# elif "." in user_line:
