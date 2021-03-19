# (14912) 숫자 빈도수
n, digit = map(int, input().split())
digit = str(digit)

count = 0
for num in range(1, n + 1):
    for char_num in str(num):
        if digit == char_num:
            count += 1

print(count)