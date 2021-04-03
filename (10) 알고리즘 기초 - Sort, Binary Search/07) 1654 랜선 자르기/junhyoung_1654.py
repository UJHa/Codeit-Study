# 1654 랜선 자르기
import sys

K, N = map(int, sys.stdin.readline().split())
line_list = []
for _ in range(K):
    line_list.append(int(sys.stdin.readline()))

count = 0  # 랜선의 현재 길이로 잘랐을때 몇 개 만들수 있는지
ans = 0  # 랜선의 최대 길이
start = 1  # 최소 길이
end = max(line_list)  # 최대 길이

while start <= end:
    length = (start + end) // 2
    count = 0

    for i in line_list:
        count += (i // length)

    # 'N 개보다 많이 만드는 것도 N 개를 만드는 것에 포함된다' 라는 문제의 조건
    if count >= N:
        start = max_length + 1
        ans = max(ans, length)

    else:
        end = length - 1

print(ans)
