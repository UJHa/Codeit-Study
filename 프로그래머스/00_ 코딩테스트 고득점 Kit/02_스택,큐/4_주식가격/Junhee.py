# 정확성 66.7 효율성 33.3 합 100 성공

from collections import deque


def solution(prices):
    answer = deque()
    deq_price = deque(prices)
    
    while deq_price:
        price = deq_price.popleft()
        tmp = 0
        for i in deq_price:
            tmp += 1
            if price > i:
                break
        answer.append(tmp)
    
    return list(answer)
