N = int(input())  # 입력

tile = [0 for _ in range(N)]  # 타일
 
for i in range(N):
    if i == 0:  # N = 1일 때 경우의 수 1
        tile[i] = 1
        continue
    elif i == 1:  # N = 2 일 때 경우의 수 3
        tile[i] = 3
        continue
    tile[i] = tile[i-1] + tile[i-2]  # 점화식 적용 
    
print(tile[N-1]%10007)
