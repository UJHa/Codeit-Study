# 주식가격(성공)
# 정확성: 66.7
# 효율성: 33.3
# 합계: 100.0 / 100.0
from collections import deque


def solution(prices):
    answer = []
    price_queue = deque(prices)

    while price_queue:
        price = price_queue.popleft()
        num = 0
        for p in price_queue:
            num += 1
            if price > p:
                break
        answer.append(num)

    return answer


s = solution([1, 2, 3, 2, 3])  # [4, 3, 1, 1, 0]
print(s)
