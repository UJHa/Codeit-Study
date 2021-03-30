'''
해결방법 1. sort() 사용

해결방법 2. 정렬 알고리즘 구현
'''

def arrange_numbers():

    n = int(input())
    num_list = []
    for i in range(n):
        num_list.append(int(input()))

    num_list.sort()

    for num in num_list:
        print(num)

    return 0

arrange_numbers()

