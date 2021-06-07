# 주식가격(실패)
# 정확성: 6.7
# 효율성: 0.0
# 합계: 6.7 / 100.0
def solution(prices):
    answer = []

    for i, p in enumerate(prices):
        count = 0   # 가격이 떨어지지 않은 기간을 저장하는 변수
        for rp in prices[i+1:]:
            if p <= rp:
                count += 1
        answer.append(count)

    return answer


s = solution([1, 2, 3, 2, 3])   # [4, 3, 1, 1, 0]
print(s)
