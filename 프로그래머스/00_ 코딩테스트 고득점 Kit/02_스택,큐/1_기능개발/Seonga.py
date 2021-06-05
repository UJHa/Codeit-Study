# 정확도 100%
'''
# 접근
1. 진도가 100%가 되기 위해 걸리는 일 수 계산
2. 뒤에 있는 기능이 앞에 있는 기능보다 더 낮은 값일 경우 앞의 기능이 걸리는 일수로 대체
3. Counter 모듈을 이용하여 동일한 일수의 개수 return 
'''

import math
from collections import Counter

def solution(progress, speeds):
    over_progress = []
    
    for i in range(len(progress)):
        over_progress.append(math.ceil((100-progress[i])/speeds[i]))  # 진행할 일수 
    
    # 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포 
    for i in range(1, len(over_progress)):
      
        if over_progress[i] < over_progress[i-1]:
            
            over_progress[i] = over_progress[i-1]
              
    return list(Counter(over_progress).values())
  

progress = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progress, speeds))
