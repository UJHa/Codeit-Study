# 입력 
_, home_N = list(map(int, input().split()))
TreeLST = list(map(int, input().split()))

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
        answer = mid_value
        start_value = mid_value + 1
            
    elif total_sum < home_N:
        end_value = mid_value -1 
            
print(answer)
            
