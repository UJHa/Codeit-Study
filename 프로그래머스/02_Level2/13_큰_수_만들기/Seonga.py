def solution(number, k):

    stack = [number[0]]

    for num in number[1:]:

        while len(stack) > 0 and stack[-1] < num and k > 0:  # 입력값이 stack 있는 값보다 크고 k 가 남아있을 때까지 반복 

            k -= 1

            stack.pop()  # 기존에 있는 값 제거 

        stack.append(num)  

    # k = 1 이고 stack 에 쌓이는 값이 항상 첫번째 인덱스가 가장 크다면 while문을 돌지 않으므로 
    if k != 0:
        for _ in range(k):
            stack.pop()

    answer = ''.join(stack)

    return str(answer)
