# 짝지어 제거하기(실패2)
# 정확성: 60.2
# 효율성: 0.0
# 합계: 60.2 / 100.0
def solution(s):
    l = list(s)
    check_index = 0
    while len(l) > 1:
        if l[check_index] != l[check_index + 1]:
            check_index += 1
        if check_index == len(l) - 1:
            break
        if l[check_index] == l[check_index + 1]:
            l.pop(check_index)
            l.pop(check_index)
            check_index = check_index > 0 and check_index - 1 or 0
    if len(l) == 0:
        answer = 1
    else:
        answer = 0

    return answer


s = solution('baabaa') == 1
# s = solution('cdcd') == 0
print(s)
