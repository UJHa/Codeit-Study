'''
시간 복잡도 : (m log m) + (log m)*n
'''

def binary_search(list_a, m, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    if list_a[mid] == m:
        return mid
    elif list_a[mid] > m:
        return binary_search(list_a, m, low, mid - 1)
    else:
        return binary_search(list_a, m, mid + 1, high)

def find_num():

    n = int(input())
    list_a = list(map(int, input().split()))
    m = int(input())
    list_m = list(map(int, input().split()))

    list_a.sort()

    for m in list_m:
        low = 0
        high = n - 1

        if binary_search(list_a, m, low, high) > -1:
            print(1)
        else:
            print(0)

    return 0

find_num()