# 입력받기
n, m = map(int, input().split())

# 122333444 와 같은 수열 생성하기 
arr = []
cnt = 0

while len(arr)<m: 
    cnt += 1 
    arr.extend([cnt]*cnt)  # cnt 값을 반복해서 수열 생성 

print(sum(arr[n-1:m]))  # n, m 까지 범위의 숫자 합 구함.
