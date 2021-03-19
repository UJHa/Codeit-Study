## 1. 8*8 체스판을 만든다.
## 2. 흰 칸의 인덱스를 받는다.
## 3. 흰 칸 인덱스에 F가 몇 개 있는지 확인한다. 
#----------------------------------------------
# 입력 받기 
arr_input = [list(input()) for _ in range(8)]

# 체스판 만들기 
arr = [[-1]*8 for _ in range(8)]

i = 0
even = ['W','B']*4
odd = ['B','W']*4

while i<len(arr):
    if i%2 == 0: # 짝수이면
        arr[i] = even
    else:
        arr[i] = odd
        
    i += 1
    
# 2. 흰 칸 위에 말이 몇 개 있는지 확인하기     
row = -1

row_index = []
col_index = []

for i in arr:
    row +=1
    col = -1
    for a in i:
        col += 1
        if a=="W":
            row_index.append(row)
            col_index.append(col)

cnt = 0

for row_index_value, col_index_value in zip(row_index, col_index):
    if arr_input[row_index_value][col_index_value] == 'F':
        cnt +=1
        
print(cnt)
