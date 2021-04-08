# (1920) 수 찾기

# 재귀 풀이
def is_in_list(num, num_lst, start, end):
    if start > end:
        return False
    else:
        center_index = (start + end) // 2
        if num_lst[center_index] < num:
            return is_in_list(num, num_lst, center_index + 1, end)
        elif num_lst[center_index] > num:
            return is_in_list(num, num_lst, start, center_index - 1)
        else:
            return True

# 반복을 통한 풀이
# def is_in_list(num, num_lst):
#     start_pos = 0
#     end_pos = len(num_lst) - 1
#     move_pos = (start_pos + end_pos) // 2
#     while start_pos <= end_pos:
#         if num_lst[move_pos] < num:
#             start_pos = move_pos + 1
#         elif num_lst[move_pos] > num:
#             end_pos = move_pos - 1
#         else:
#             return True
#         move_pos = (start_pos + end_pos) // 2
#
#     return False


n = int(input())

num_list = list(map(int, input().split()))

num_list.sort()

m = int(input())
check_list = list(map(int, input().split()))

for ch in check_list:
    if is_in_list(ch, num_list, 0, len(num_list) - 1):
    # if is_in_list(ch, num_list):
        print(1)
    else:
        print(0)