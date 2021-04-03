# 수찾기와 동일한데 왜 틀렸는지 모르겠음.

# 이진탐색 
def binary_search(value, lst, start_index = 0, end_index = None):
    
    if end_index == None:
        end_index = len(lst)-1

    mid_point = (start_index+end_index)//2
    
    if start_index > end_index:
        return 0
    
    if value == lst[mid_point]:
        return 1
    
    elif value > lst[mid_point]:
        return binary_search(value, lst, start_index = mid_point + 1, end_index = end_index)
    elif value < lst[mid_point]:
        return binary_search(value, lst, start_index = 0, end_index = mid_point - 1)

T = int(input())

N = int(input())
LST1= list(map(int, input().split()))

M = int(input())
LST2= list(map(int, input().split()))

# quicksort(LST1)
LST1.sort()

for value in LST2:
    print(binary_search(value, LST1))
    
