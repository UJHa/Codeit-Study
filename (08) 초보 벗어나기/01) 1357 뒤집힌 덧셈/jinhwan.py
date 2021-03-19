# (1357) 뒤집힌 덧셈
x, y = map(str, input().split())
result = int(x[::-1]) + int(y[::-1])
result = str(result)[::-1]
print(int(result))