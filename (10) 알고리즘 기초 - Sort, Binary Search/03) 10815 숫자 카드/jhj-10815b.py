'''
1950번과 같은 문제
다만 범위가 정수임
'''

def binary_search(list_a, m, low, high):
    if low > high:
        return "a"

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
    list_answer = []

    list_a.sort()

    for m in list_m:
        low = 0
        high = n - 1

        if type(binary_search(list_a, m, low, high)) == str:
            print(0, end=' ')
        else:
            print(1, end=' ')

    return 0

find_num()