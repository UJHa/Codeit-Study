# 체육복
def solution(n, lost, reserve):
    answer = 0
    wear_list = [1 for _ in range(n)]
    for i in range(n):
        if i+1 in lost:
            wear_list[i] -= 1
        if i+1 in reserve:
            wear_list[i] += 1

    for i, w in enumerate(wear_list):
        if w == 2:
            if i - 1 >= 0 and wear_list[i - 1] == 0:
                wear_list[i - 1] += 1
                wear_list[i] -= 1
            elif i + 1 < len(wear_list) and wear_list[i + 1] == 0:
                wear_list[i + 1] += 1
                wear_list[i] -= 1

    for w in wear_list:
        if w != 0:
            answer += 1

    return answer


s = solution(5, [2, 4], [1, 3, 5]) == 5
print(s)