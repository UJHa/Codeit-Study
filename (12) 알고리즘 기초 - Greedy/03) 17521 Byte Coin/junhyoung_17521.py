# 17521 Byte Coin
# 메모리 : 28776 KB, 시간 : 68 ms
# 문제 링크 : https://www.acmicpc.net/problem/17521
"""
살때 : 값이 떨어지고 있는 상태일때 다음날 오르면 삼

팔때 : 값이 올라가고 있는 상태일때 다음날 떨어지면 삼

마지막날에는 가지고 있는 코인 다 팔것
"""

import sys

n, my_wallet = map(int, sys.stdin.readline().split())
coin_list = []
for _ in range(n):
    coin_list.append(int(sys.stdin.readline()))

rise = False  # 전날보다 오늘 값이 높다면 -> 오름 상태 -> rise = True
coin_count = 0  # 내가 몇 주 가지고 있는지

for i in range(n - 1):
    # 떨어지고 있는 상태일때, 다음날 값이 오늘보다 높아진다면 산다 -> 최저가에 산다
    if coin_list[i] < coin_list[i + 1] and rise is False:
        coin_count = my_wallet // coin_list[i]
        my_wallet = my_wallet % coin_list[i]
        rise = True

    # 오름 상태인데, 다음날 값이 오늘보다 떨어진다면 판다 -> 최고치에 판다
    elif coin_list[i] > coin_list[i + 1] and rise is True:
        my_wallet += coin_list[i] * coin_count
        coin_count = 0
        rise = False

    # print(coin_count, price)

# 마지막 일차에 내가 가지고 있는 코인의 개수를 모두 팜
my_wallet += coin_list[-1] * coin_count
print(my_wallet)
