a, b, c, n = map(int, input().split())
ans = 0
# 각 방을 꽉 채우는 것을 기준으로 학생 수를 센다
for i in range(0, n + 1, a):
    for j in range(0, n + 1, b):
        for k in range(0, n + 1, c):
            # 세 방의 학생 수 합이 일치하면 1
            if i + j + k == n: ans = 1
print(ans)