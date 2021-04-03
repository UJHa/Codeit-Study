# 이진탐색을 재귀함수로 구현하면 시간초과
from sys import stdin

# 이진탐색 
def binary_search(value, lst, start_index = 0, end_index = None):
     
    end_index = len(lst) -1
    
    while start_index<= end_index:
        mid_index = (start_index+end_index)//2
        
        if lst[mid_index] == value:
            return 1
        elif lst[mid_index] > value:
            end_index = mid_index - 1
        elif lst[mid_index] < value:
            start_index = mid_index + 1
            
    return 0
    

T = int(stdin.readline())  # 테스트 개수만큼 돌아가야함.

for i in range(T):

    N = int(stdin.readline())
    LST1= list(map(int, stdin.readline().split()))

    M = int(stdin.readline())
    LST2= list(map(int, stdin.readline().split()))

    LST1.sort()

    for value in LST2:
        print(binary_search(value, LST1))
    
