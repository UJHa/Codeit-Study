import sys

# 숫자 카드가 최대 500,000개까지 들어올 수 있으므로
# sys를 사용해 입력수행시간 최적화
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
# 이진 탐색을 위한 정렬 
arr.sort()

for i in list(map(int, sys.stdin.readline().split())):
    start = 0
    end = N - 1
    # 상근이가 가지고 있는 카드인지 확인하는 flag
    flag = 0

    while start <= end:
        mid = (start + end) // 2
        if i == arr[mid]:
            print(1, end = ' ')
            flag = 1
            break
        elif i < arr[mid]: end = mid - 1
        else: start = mid + 1
        
    if flag == 0: print(0, end = ' ')
print()