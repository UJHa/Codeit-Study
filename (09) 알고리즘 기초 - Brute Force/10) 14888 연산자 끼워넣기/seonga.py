def candy_operator(n, arr, op_arr):
    
    lst = []
    
    for i in range(4): # 0: +, 1: -, 2: *, 3: //  -> 순서가 있으므로 순열 사용 
        for j in range(op_arr[i]):
            lst.append(i)  # 연산자 리스트 생성  
            
    from itertools import permutations
    
    operator = set(list(permutations(lst, 2)))  # 연산자 추출 후 중복 제거 
    
    # 항상 -10억보다 크거나 같고 10억보다 작거나 같은 결과가 나오는 입력만 주어짐. 
    max_value = 10000000
    min_value = -10000000
    
    for candy_op in operator:
        answer = arr[0]  # 주어진 수의 순서를 바꾸면 안됨. 
        for i in range(len(candy_op)):
            if candy_op[i] == 0:
                answer = answer + arr[i+1]
            elif candy_op[i] == 1:
                answer = answer - arr[i+1]
            elif candy_op[i] == 2:
                answer = answer * arr[i+1]
            else:
                answer = answer // arr[i+1]
                
        max_value = max(max_value, answer)  # 최댓값
        min_value = min(min_value, answer)  # 최솟값
    
    return max_value, min_value
            
n = int(input())
num_arr = list(map(int, input().split()))
op_arr = list(map(int, input().split()))

max_, min_ = candy_operator(n, num_arr, op_arr)   
  
print(max_)
print(min_)   
