def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if str(i**0.5)[-2:] == '.0':
            answer -= i
        else:
            answer += i
    return answer
