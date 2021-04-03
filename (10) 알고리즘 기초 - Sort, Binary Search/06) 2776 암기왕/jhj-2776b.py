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
    memo1 = []
    memo2 = []

    for i in range(t):
        n = int(input())
        memo1.append(list(map(int, input().split())))
        m = int(input())
        memo2.append(list(map(int, input().split())))

    for case in range(t):
        memo1[case].sort()

        for num in memo2[case]:
            if binary_search(memo1[case], num, low = 0, high = n - 1) > -1:
                print(1)
            else:
                print(0)

    return 0

compare_memo()