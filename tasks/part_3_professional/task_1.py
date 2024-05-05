sumbels: str = '~' * 5
user_line: str = input()

length: int = len(user_line) + 10
result: str = f'{user_line:~^{length}}'
print(result)
