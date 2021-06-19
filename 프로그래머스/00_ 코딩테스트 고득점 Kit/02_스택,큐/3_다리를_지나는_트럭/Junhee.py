# 미완성 코드 

# 1. trucks에서 첫 번째 트럭을 뽑아 다리 위에 올린다
# 2. 다음 트럭을 올릴 수 있는지 검증한다
# 2-1. 올릴 수 있다면, 이미 올린 트럭들에 모두 -1하고 올린다
# 2-2. 올릴 수 없다면, 이미 올린 트럭들 중 맨 앞을 내리고 다시 2로 간다
# 3. 다리와 trucks에 트럭이 없다면 종료하고, 있다면 2로 간다
from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks = deque(truck_weights)
    bridge = deque()
    bridge_weight = deque()

    # 첫 번째 트럭 올리기 
    bridge.append(bridge_length-1)
    bridge_weight.append(trucks[0])
    weight -= trucks.popleft()
    answer += 1

    while trucks and bridge:
        # 다음 트럭을 올릴 수 있는 경우 
        if trucks[0] <= weight and len(bridge) <= bridge_length:
            for i, j in enumerate(bridge):
                bridge[i] -= 1
            bridge.append(bridge_length-1)
            bridge_weight.append(trucks[0])
            weight -= trucks.popleft()
            answer += 1
        
        # 다음 트럭을 올릴 수 없는 경우
        else:
            length = bridge.popleft()
            for i, j in enumerate(bridge):
                bridge[i] -= length

    return answer


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))