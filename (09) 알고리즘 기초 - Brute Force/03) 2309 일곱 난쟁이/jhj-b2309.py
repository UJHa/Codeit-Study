def find_true():

    height = []
    for i in range(9):
        height.append(int(input()))

    sum_height = sum(height)

    for i in range(8): # 제거 난쟁이 찾기
        for j in range(i+1, 9):
            if sum_height - height[i] - height[j] == 100:
                record = [i, j]

    height.pop(record[0])
    height.pop((record[1] - 1)) # 난쟁이 제거
    height.sort()

    for i in range(7):
        print(height[i])

    return 0


find_true()
