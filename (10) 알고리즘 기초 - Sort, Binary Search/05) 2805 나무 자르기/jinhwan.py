# (2805) 나무 자르기 - Binary Search
def get_tree_length(tree_list, height):
    sum_length = 0
    for tree in tree_list:
        if tree > height:
            sum_length += tree - height
    return sum_length


def get_cut_height(tree_list, target_length):
    start = 1
    end = max(tree_list)
    result = 0

    while start <= end:
        mid = (start + end) // 2
        sum_height = get_tree_length(tree_list, mid)

        if sum_height < target_length:
            end = mid - 1
        elif sum_height > target_length:
            result = max(result, mid)
            start = mid + 1
        else:
            return mid
    return result


# 입력에 대한 처리
n, m = map(int, input().split())

tree_heights = list(map(int, input().split()))

print(get_cut_height(tree_heights, m))
