n, m = map(int,input().split())
arr_input = [list(input()) for _ in range(n)]

arr = [[-1]*8 for _ in range(8)]

i = 0

w_board = ['W','B']*4
b_board = ['B','W']*4

while i<len(arr):
    if arr_input[0][0] =="W":
        if i%2 == 0: # 짝수이면
            arr[i] = w_board
        else:
            arr[i] = b_board
    else:
        if i%2 == 0: # 짝수이면
            arr[i] = b_board
        else:
            arr[i] = w_board
    
    i += 1

# 문제 재확인
# 어디서 시작하던지 상관없음!! ! -> 이 부분 고려해서 다시 해결하기
min_count = 64

count = 0
if n*m>64:
    count += n*m-64
for i in range(8):
    for j in range(8):
        if arr[i][j] != arr_input[i][j]:
            count+=1
print(count)
