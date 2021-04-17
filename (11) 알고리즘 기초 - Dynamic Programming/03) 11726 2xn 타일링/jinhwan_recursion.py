# (11726) 2xn 타일링 - 재귀 풀이(top down)
import sys

# 재귀 깊이 기본값은 1000으로 문제 요구사항인 100000보다 작기 때문에 설정값 변경
sys.setrecursionlimit(10**5)

fill_dict = {}


def get_fill_rect_count(num):
    if num == 1:
        fill_dict[num] = 1
    elif num == 2:
        fill_dict[num] = 2
    elif fill_dict.get(num) is None:
        fill_dict[num] = get_fill_rect_count(num - 1) + get_fill_rect_count(num - 2)

    return fill_dict[num]


# 입력에 대한 처리
n = int(input())
print(get_fill_rect_count(n) % 10007)