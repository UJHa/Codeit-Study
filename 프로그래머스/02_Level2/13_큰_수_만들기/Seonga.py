
def solution(number, k):
    
    stack = [number[0]]

    for num in number[1:]:

        while len(stack) > 0 and stack[-1] < num and k > 0:  # 입력값이 stack 있는 값보다 크고 k 가 남아있을 때까지 반복 

            k -= 1

            stack.pop()  # 기존에 있는 값 제거 

        stack.append(num)  

    answer = ''.join(stack)

    return str(answer)
