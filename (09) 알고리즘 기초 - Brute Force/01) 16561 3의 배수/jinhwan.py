# (16561) 3의 배수
n = int(input())

count = 0
for i in range(3, n + 1, 3):
    for j in range(3, n + 1, 3):
        k = n - i - j
        if k >=3 and k % 3 == 0:
            count += 1

print(count)