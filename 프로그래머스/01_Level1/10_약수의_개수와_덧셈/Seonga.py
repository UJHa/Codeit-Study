def solution(left, right):

    answer = 0

    for value in range(left, right +1):
        cnt = 0

        for i in range(1, value+1):
            if value % i == 0:
                cnt += 1

        if cnt % 2 == 0:
            answer += value
        else:
            answer -= value
        
    return answer
