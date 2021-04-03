
from sys import stdin

_, N = map(int, stdin.readline().split())
LAN_LST = list(map(int, stdin.readlines()))

start_value = 1   # 0으로 하면 zero division error 발생 
end_value = max(LAN_LST) 
answer = 0  # 랜선 최대 길이를 담을 변수 

while start_value <= end_value:  
    
    mid_value = (start_value + end_value)//2  # 랜선의 최대 길이를 찾을 변수 
    total_sum  = 0
    
    for value in LAN_LST: 
        total_sum += value//mid_value  # 보유하고 있는 랜선을 각각 자를 랜선으로 나눠지는 개수 합 
        
    # 나눠진 후 생기는 랜선의 개수를 필요한 랜선의 개수와 비교
    if total_sum >= N:  
        answer = max(answer, mid_value)   # 최대 
        start_value = mid_value + 1
            
    elif total_sum < N:
        end_value = mid_value -1 
            
print(answer)
            

