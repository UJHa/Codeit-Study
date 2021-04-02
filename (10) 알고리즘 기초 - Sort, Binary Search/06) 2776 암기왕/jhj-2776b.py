'''
수 찾기와 동일
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

def compare_memo():

    t = int(input())
    n = int(input())
    memo1 = list(map(int, input().split()))
    m = int(input())
    memo2 = list(map(int, input().split()))

    memo1.sort()

    for num in memo2:
        if binary_search(memo1, num, low = 0, high = n - 1) > -1:
            print(1)
        else:
            print(0)

    return 0

compare_memo()