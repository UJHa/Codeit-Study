# python3 시간초과
# pype3로 작동

from sys import stdin

_, home_N = map(int, stdin.readline().split())
TreeLST = list(map(int, stdin.readline().split()))

# 자를 나무(H)의 최소 길이, 최대길이까지를 start_value, end_value로 둠
start_value = 1
end_value = max(TreeLST)-1

answer = 0  # 정답 H를 담을 변수

# start_value, end_value의 사이 값들로 잘라가며 H를 구함 
while start_value <= end_value:
    
    mid_value = (start_value + end_value)//2
    
    total_sum = 0
    
    for i in range(len(TreeLST)):
        if TreeLST[i] > mid_value:
            total_sum += TreeLST[i] - mid_value
        
    if total_sum >= home_N:
        answer = max(answer, mid_value)  # max함수를 적용하지 않아도 최대값이 나옴 -> 정렬된 값을 사용해서 그런듯
        start_value = mid_value + 1
            
    elif total_sum < home_N:
        end_value = mid_value -1 
            
print(answer)
            
