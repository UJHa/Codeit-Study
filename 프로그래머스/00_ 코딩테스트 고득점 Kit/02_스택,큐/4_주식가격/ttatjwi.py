정확성: 66.7
효율성: 0.0
합계: 66.7 / 100.0

def solution(prices):
    answer = []
    count = 0

    for i,j in enumerate(prices):
        while True:
            #끝까지 가격이 올라갔을 때
            if i + count == len(prices)-1:
                answer.append(count)
                count = 0
                break
            #마지막 주식밖에 안 남았을 때
            elif i == len(prices)-1:
                answer.append(0)
                break
            #가격이 상승할 때
            elif j <= prices[i+1+count]:
                count += 1
            #가격이 하락할 때
            else:
                count += 1
                answer.append(count)
                count = 0
                break

    return answer
