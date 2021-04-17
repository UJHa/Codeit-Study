N = int(input())  # 입력

tile = [0 for _ in range(N)]  # 타일
 
for i in range(N):
    if i == 0:  # 입력받은 N이 1일 때 -> 2x1 사각형
        tile[i] = 1
        continue
    elif i == 1:  # 입력받은 N이 2일 때 -> 2x2 사각형
        tile[i] = 2
        continue
    tile[i] = tile[i-1] + tile[i-2]  # 점화식 적용 
    
print(tile[N-1]%10007)
