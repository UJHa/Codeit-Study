# 2차 실패(정확성은 100%, 효율성 0%)
# 1차 방식 : info 데이터 내부의 columns 하나씩 비교하는 방식
# 2차 방식 : info의 column들을 가져와서 일치하는 데이터의 index에 접근하여 비교하는 방식
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
    result = [i for i in range(len(info))]
    score_index = len(query) - 1
    for i, q in enumerate(query):
        if i != score_index:
            result = get_true_list(q, [data[i] for data in info], result)
        else:
            result = get_true_score_list(q, [data[i] for data in info], result)

    return len(result)


def get_true_list(query_data, column_list, true_list):
    result = []
    for i in true_list:
        if column_list[i] == query_data or query_data == '-':
            result.append(i)
    return result


def get_true_score_list(query_data, column_list, true_list):
    result = []
    for i in true_list:
        if int(column_list[i]) >= int(query_data):
            result.append(i)
    return result


def solution(info, query):
    answer = []

    query_list = get_query_list(query)
    info_list = [i.split() for i in info]

    for q in query_list:
        answer.append(get_query_count(info_list, q))

    return answer


#1,1,1,1,2,4
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
               ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))