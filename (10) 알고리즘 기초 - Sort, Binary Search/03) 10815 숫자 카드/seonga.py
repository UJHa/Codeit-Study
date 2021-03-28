# 퀵 정렬과 이진탐색을 이용하여 문제 풀이 

# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    
    # 리스트 값 확인과 기준점 이하 값들의 위치 확인을 위한 변수 정의
    i = start  # small
    b = start  # big 
    p = end  # pivot 

    # start와 end가 겹치지 않을 때까지 
    while i < p:
        # i 인덱스의 값이 기준점보다 작으면 i와 b 인덱스에 있는 값들을 교환하고 b를 1 증가 시킨다
        if my_list[i] <= my_list[p]:
            swap_elements(my_list, i, b)
            b += 1
        i += 1

    # b와 기준점인 p 인덱스에 있는 값들을 바꿔준다
    swap_elements(my_list, b, p)
    p = b

    # pivot의 최종 인덱스를 리턴해 준다
    return p


# 퀵 정렬
def quicksort(my_list, start = 0, end = None):
    
    if end == None:
        end = len(my_list)-1
    
    # 코드를 작성하세요.
    if end - start < 1:
        return  # return 뒤에 아무것도 없으면 return None
    
    pivot = partition(my_list, start, end) # pivot의 인덱스 받기
    
    quicksort(my_list, start, pivot -1)  # pivot기준으로 왼쪽
    quicksort(my_list, pivot+1, end)  # pivot기준으로 오른쪽 
    
    return 

# 이진탐색
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
quicksort(ANSWER_A)

M = int(input())
ANSWER_M = list(map(int, input().split()))

# 출력하기 
for num in ANSWER_M:
    print(Binary_search(num, ANSWER_A))
