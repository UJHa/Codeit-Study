# (2805) 나무 자르기 - Brute Force
# 최대 높이부터 1씩 내려가면서 찾기(시간 초과됩니다. 구현 방식만 참고하면 될 것 같습니다.)
def get_tree_length(tree_list, height):
    sum_length = 0
    for tree in tree_list:
        if tree <= height:
            continue
        else:
            sum_length += tree - height
    return sum_length


def get_cut_height(tree_list, target_length):
    max_height = max(tree_list)
    for i in range(max_height, 0, -1):
        if target_length == get_tree_length(tree_list, i):
            return i
    return 0


# 입력에 대한 처리
n, m = map(int, input().split())

tree_heights = list(map(int, input().split()))

print(get_cut_height(tree_heights, m))