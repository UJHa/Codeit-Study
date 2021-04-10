# (17212) 달나라 토끼 문제 - 반복문 풀이(bottom up)
def pay_count(num):
    pay_dict = {}
    pay_coins = [7, 5, 2, 1]
    for i in range(num + 1):
        if i == 0:
            pay_dict[i] = 0
        else:
            min_value = 100000
            for coin in pay_coins:
                if i >= coin:
                    min_value = min(min_value, pay_dict[i - coin] + 1)
            pay_dict[i] = min_value

    return pay_dict[num]


# 입력에 대한 처리
n = int(input())
print(pay_count(n))