from itertools import combinations


def get_tuple_list(row_list, count):
    result = {}
    index_list = [i for i in range(len(row_list))]
    for indexs in combinations(index_list, count):
        temp_list = []
        for i in range(len(row_list[0])):
            data = []
            for j in indexs:
                data.append(row_list[j][i])
            temp_list.append(tuple(data))

        result[indexs] = temp_list
    return result


def solution(relation):
    answer = 0
    col_list = [[] for _ in range(len(relation[0]))]
    for re in relation:
        for j, data in enumerate(re):
            col_list[j].append(data)

    # 2개 이상인 유일키
    count = 1
    answer_list = []
    while len(col_list) >= count:
        print(count)
        t_list = get_tuple_list(col_list, count)
        for k, v in t_list.items():
            subset_check = False
            for a in answer_list:
                if set(a).issubset(set(k)):
                    subset_check = True
            if subset_check is True:
                continue

            if len(v) == len(set(v)):
                answer += 1
                answer_list.append(k)

        count += 1

    return answer


# s = solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],
#               ["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])
s = solution([['a', 'aa'], ['aa', 'a'], ['a', 'a']])
print(s)