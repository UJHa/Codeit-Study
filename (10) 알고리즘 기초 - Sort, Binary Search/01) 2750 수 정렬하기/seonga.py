# 합병정렬로 정렬

# 입력받기 
N = int(input())
ANSWER = [int(input()) for _ in range(N)]

def merge(list1, list2):
    i = 0
    j = 0

    # 정렬된 항목들을 담을 리스트
    merged_list = []

    # list1과 list2를 돌면서 merged_list에 항목 정렬
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i += 1

    # list2에 남은 항목이 있으면 정렬 리스트에 추가
    if i == len(list1):
        merged_list += list2[j:]

    # list1에 남은 항목이 있으면 정렬 리스트에 추가
    elif j == len(list2):
        merged_list += list1[i:]

    return merged_list  
    
# 합병 정렬
def merge_sort(my_list):
    # base case: list에 값이 0개 또는 1개 일 때
    if len(my_list) < 2:
        return my_list
    
    # Divide
    mid_point = len(my_list)//2
   
    left_lst = my_list[:mid_point]
    right_lst = my_list[mid_point:]
    
    # Combine, Conquer
    return merge(merge_sort(left_lst), merge_sort(right_lst))

# 하나씩 출력 
for n in merge_sort(ANSWER):
    print(n)
