#1차 실패(정확성은 100%, 효율성 0%)>> 속도 개선 필요
def get_query_list(query):
    result = []
    query_list = [q.split() for q in query]
    for q in query_list:
        query_data = []
        for data in q:
            if data != 'and':
                query_data.append(data)
        result.append(query_data)
    return result


def get_query_count(info, query):
    result = 0
    for i in info:
        print(i)
        if is_true_data(i, query):
            result += 1

    return result


def is_true_data(data, query):
    if int(query[-1]) > int(data[-1]):
        return False
    for i, q in enumerate(query):
        if query[i] == '-' or query[i] == data[i]:
            continue
        else:
            if i == len(query) - 1:
                return True
            else:
                return False

    return True


def solution(info, query):
    answer = []

    query_list = get_query_list(query)
    info_list = [i.split() for i in info]

    for q in query_list:
        print(q)
        answer.append(get_query_count(info_list, q))

    return answer


#1,1,1,1,2,4
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
               ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))