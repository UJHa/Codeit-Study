# 기능개발 (성공)
# 정확성: 100.0
# 합계: 100.0 / 100.0
import math


def solution(progresses, speeds):
    answer = []

    prev_days = 0
    for p, s in zip(progresses, speeds):
        work_days = math.ceil((100 - p) / s)
        if work_days > prev_days:
            answer.append(1)
            prev_days = work_days
        else:
            answer[-1] += 1

    return answer


s = solution([93, 30, 55], [1, 30, 5])  # [2, 1]
print(s)
