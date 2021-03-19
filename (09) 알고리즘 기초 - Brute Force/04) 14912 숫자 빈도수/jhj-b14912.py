def how_many():

    n, d = map(int, input().split())
    result = 0

    number_list = []
    calc_list = []
    for i in range(1, n + 1): number_list.append(str(i))
    for i in range(len(number_list)):
        for j in range(len(number_list[i])):
            calc_list.append(number_list[i][j])

    for i in calc_list:
        if i == str(d):
            result += 1

    print(result)

    return 0


how_many()