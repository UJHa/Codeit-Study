# 짝지어 제거하기(성공) : 스택을 활용한 풀이
# 정확성: 60.2
# 효율성: 39.8
# 합계: 100.0 / 100.0
def solution(s):
    stack = []
    for c in s:
        if len(stack) > 0 and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    print(stack)
    answer = -1
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0

    return answer


s = solution('baabaa') == 1
# s = solution('cdcd') == 0
print(s)
