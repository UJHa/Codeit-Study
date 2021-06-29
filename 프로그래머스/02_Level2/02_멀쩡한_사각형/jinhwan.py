# 멀쩡한 사각형
# 정확성: 100.0
# 합계: 100.0 / 100.0
import math


def solution(w, h):
    if w == 1 or h == 1:
        return 0
    if w == h:
        return w * h - w

    start_y, end_y = 0, 0
    not_use_count = 0
    for x in range(1, w+1):
        end_y = h * x / w
        not_use_count += int(math.ceil(end_y) - (start_y // 1))
        start_y = end_y

    answer = w * h - not_use_count
    return answer


s = solution(8, 12) == 80
print(s)