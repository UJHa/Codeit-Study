# 주식가격(실패)
# 정확성: 66.7(10/10)
# 효율성: 0.0(5/5) 시간 초과
# 합계: 66.7 / 100.0
def solution(prices):
    answer = []
    prices_count = len(prices)
    for i, p in enumerate(prices):
        is_consecutive = True
        end_index = 0
        for j, rp in zip(range(i + 1, prices_count), prices[i + 1:]):
            if rp < p:
                is_consecutive = False
                end_index = j
                break
        if is_consecutive:
            answer.append(prices_count - 1 - i)
        else:
            answer.append(end_index - i)

    return answer


s = solution([1, 2, 3, 2, 3])  # [4, 3, 1, 1, 0]
print(s)
