# (11726) 2xn 타일링 - 반복문 풀이(bottom up)
def get_fill_rect_count(num):
    fill_dict = {}
    for i in range(1, num + 1):
        if i == 1:
            fill_dict[i] = 1
        elif i == 2:
            fill_dict[i] = 2
        else:
            fill_dict[i] = fill_dict[i - 1] + fill_dict[i - 2]

    return fill_dict[num]


# 입력에 대한 처리
n = int(input())
print(get_fill_rect_count(n) % 10007)