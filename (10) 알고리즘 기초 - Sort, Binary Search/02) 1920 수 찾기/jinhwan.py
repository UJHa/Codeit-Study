# (1920) 수 찾기
def is_in_list(num_lst, num):
    # 문제 풀기 진행중...(시간 초과)
    # if len(num_lst) <= 2:
    #     return num in num_lst
    # else:
    #     center_index = len(num_lst) // 2
    #     if num_lst[center_index] < num:
    #         return is_in_list(num_lst[center_index+1:], num)
    #     elif num_lst[center_index] > num:
    #         return is_in_list(num_lst[:center_index-1], num)
    #     else:
    #         return True
    start_pos = 0
    end_pos = len(num_lst)
    move_pos = (start_pos + end_pos) // 2
    while 0 <= move_pos < len(num_lst):
        if num_lst[move_pos] < num:
            start_pos = move_pos + 1
        elif num_lst[move_pos] > num:
            end_pos = move_pos - 1
        else:
            return True
        move_pos = (start_pos + end_pos) // 2

    return False


n = int(input())

num_list = list(map(int, input().split()))
# print(num_list)

num_list.sort()

m = int(input())
check_list = list(map(int, input().split()))

for ch in check_list:
    if is_in_list(num_list, ch):
        print(1)
    else:
        print(0)