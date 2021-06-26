def solution(a, b):
    answer = 0
    lgth = len(a)
    for i in range(lgth):
        answer += a[i]*b[i]
    return answer
