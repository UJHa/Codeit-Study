def solution(n,a,b):
    answer = 0

    while a!=b:
        a, b = (a+1)//2, (b+1)//2  # 2의 지수 승으로 부전승은 발생하지 않으므로 2로 나누면서 라운드 확인 가능 
        
        answer += 1

    return answer
