def partitian():

    n = int(input())
    n_divided = n // 3
    result = 0

    for i in range(1, n_divided - 1): # 1부터 n-2까지 카운트
        for j in range(1, n_divided - i):
            result += 1

    print(result)

    return 0

partitian()
