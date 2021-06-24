# 내적
def solution(a, b):
    answer = 0
    for x, y in zip(a, b):
        answer += x * y
    return answer
    # return sum([x * y for x, y in zip(a, b)])


# s = solution([1, 2, 3, 4], [-3, -1, 0, 2]) == 3
s = solution([-1, 0, 1], [1, 0, -1]) == -2
print(s)
