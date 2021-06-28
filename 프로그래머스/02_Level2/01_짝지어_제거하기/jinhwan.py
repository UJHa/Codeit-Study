# 짝지어 제거하기(실패)
# 정확성: 30.3
# 효율성: 0.0
def solution(s):
    check_index = 0
    while len(s) > 1:
        if s[check_index] != s[check_index+1]:
            check_index += 1
        if check_index == len(s) - 1:
            break
        if s[check_index] == s[check_index+1]:
            s = s[:check_index] + s[check_index+2:]
            check_index = 0
    if len(s) == 0:
        answer = 1
    else:
        answer = 0

    return answer


s = solution('baabaa') == 1
# s = solution('cdcd') == 0
print(s)