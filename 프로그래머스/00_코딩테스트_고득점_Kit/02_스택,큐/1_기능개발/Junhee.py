# 정확성 100 합계 100
# progresses와 speeds 각각의 deque을 만들어 queue를 구현

from collections import deque


def solution(progresses, speeds):
    answer = []
    dq_pro = deque(progresses)
    dq_spd = deque(speeds)
    
    while dq_pro:
        ans = 0
        # 각 작업 진도 더하기
        for i, j in enumerate(dq_spd):
            dq_pro[i] += j

        # 배포
        if dq_pro[0] >= 100:
            while dq_pro:
                if dq_pro[0] < 100:
                    break
                dq_pro.popleft()
                dq_spd.popleft()
                ans += 1
                
        if ans:
            answer.append(ans)
    
    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))