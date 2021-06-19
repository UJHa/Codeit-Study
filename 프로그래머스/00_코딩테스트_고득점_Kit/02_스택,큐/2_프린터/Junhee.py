# 실패 
# Key값이 중복되어 틀리는 것으로 보임 

from collections import deque


def printing(dq):
    order = []
    while dq:
        # 우선순위 고려하여 프린트할 문서 결정(맨 앞으로)
        i = 1
        while True:
            print(dq)

            if dq[0][0] < dq[i][0]:  # Index Error 발생!
                dq.append(dq[0])
                dq.popleft()
                i = 1
            else:
                i += 1

            # 프린트 및 순서기록
            order.append(dq[0][1])
            dq.popleft()
        
    return order


def solution(priorities, location):
    # 식별가능한 문서열 만들기
    # (priority, location)
    dic = {}
    for i, j in enumerate(priorities):
        dic[j] = i
    dq = deque(list(dic.items()))
    
    order = printing(dq)
    
    return order.idex(location)


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))