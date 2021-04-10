# (17212) 달나라 토끼 문제 - 재귀 풀이(top down)
import sys

# 재귀 깊이 기본값은 1000으로 문제 요구사항인 100000보다 작기 때문에 설정값 변경
sys.setrecursionlimit(10**5)

pay_dict = {}


def pay_count(n):
    if n == 0:
        return 0

    if pay_dict.get(n) is not None:
        return pay_dict[n]
    else:
        min_value = 100000
        pay_coins = [7, 5, 2, 1]
        for coin in pay_coins:
            if n >= coin:
                min_value = min(min_value, pay_count(n - coin) + 1)
        pay_dict[n] = min_value
        return pay_dict[n]


# 입력에 대한 처리
n = int(input())
print(pay_count(n))