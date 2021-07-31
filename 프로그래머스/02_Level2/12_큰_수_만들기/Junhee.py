def solution(number, k):
    '''k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자
    1. Stack을 활용해 number 중 가장 큰 수가 맨 앞으로 올 수 있도록 한다. 
    2. 나머지 후순위 수들을 합쳐 완성한다 
    '''
    stack = [number[0]]

    for num in number[1:]:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
    
        stack.append(num)

    if k != 0:
        stack = stack[:-k]

    return ''.join(stack)

