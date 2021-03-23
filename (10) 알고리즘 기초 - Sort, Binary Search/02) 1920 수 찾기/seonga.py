# 1. 합병정렬로 리스트 정렬
# 2. 이진탐색 
## 3172ms

# 합병정렬 
def merge(left_lst, right_lst):
    
    i = 0
    j = 0
    
    merged_lst = []
    
    while len(left_lst) > i and len(right_lst) > j:
        if left_lst[i] > right_lst[j]:
            merged_lst.append(right_lst[j])
            j += 1
        else: 
            merged_lst.append(left_lst[i])
            i += 1
            
    if len(left_lst) == i:
        merged_lst += right_lst[j:]
    if len(right_lst) == j:
        merged_lst += left_lst[i:]
    
    return merged_lst

def merge_sort(lst):
    
    if len(lst) < 2:
        return lst
    
    mid_point = len(lst)//2
    
    return merge(merge_sort(lst[:mid_point]), merge_sort(lst[mid_point:]))

def Binary_search(value, lst, start_index = 0, end_index = None):
    
    if end_index == None:
        end_index = len(lst)-1

    mid_point = (start_index+end_index)//2
    
    if start_index > end_index:
        return 0
    
    if value == lst[mid_point]:
        return 1
    
    elif value > lst[mid_point]:
        return Binary_search(value, lst, start_index = mid_point + 1, end_index = end_index)
    elif value < lst[mid_point]:
        return Binary_search(value, lst, start_index = 0, end_index = mid_point - 1)
 
# 입력받기 
N = int(input())
ANSWER_A = list(map(int, input().split()))
merge_list = merge_sort(ANSWER_A)

M = int(input())
ANSWER_M = list(map(int, input().split()))

# 출력하기 
for num in ANSWER_M:
    print(Binary_search(num, merge_list))
