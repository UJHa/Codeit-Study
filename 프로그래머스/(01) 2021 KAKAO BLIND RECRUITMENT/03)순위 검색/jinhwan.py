# 3차 실패(정확성은 100%, 효율성 0%)
# 1차 방식 : info 데이터 내부의 columns 하나씩 비교하는 방식
# 2차 방식 : info의 column들을 가져와서 일치하는 데이터의 index에 접근하여 비교하는 방식
# 3차 방식 : info의 점수를 뺀 나머지 데이터를 문자열 키로 dictionary 생성, query로 key를 만들어서 dict의 value(list)에서 점수가 query score이상인 갯수 반환 방식

import itertools


def get_query_list(query):
    result = []
    query_list = [q.split() for q in query]
    for q in query_list:
        score = int(q[-1])
        q_data = q[:-1]

        query_key = ''
        for data in q_data:
            if data != 'and' and not data.isdigit():
                query_key += data
        result.append((query_key, score))
    return result


def make_info_dict(info):
    result = {}
    info_list = [i.split() for i in info]
    for i, v in enumerate(info_list):
        score = int(v[-1])
        data = v[:-1]
        keys = get_info_key_list(data)

        for k in keys:
            if result.get(k) is None:
                result[k] = [(i, score)]
            else:
                result[k].append((i, score))
    return result


def get_info_key_list(data):
    result = []
    for i in range(5):
        for j in itertools.combinations([0, 1, 2, 3], i):
            temp_data = list(data)
            for column in j:
                temp_data[column] = '-'
            result.append(''.join(temp_data))
    return result


def get_data_count(data_list, q_score):
    result = 0
    data_list.sort(key=lambda x: x[1], reverse=True)

    for d in data_list:
        d_score = d[1]
        if q_score <= d_score:
            result += 1
        else:
            break

    return result


def solution(info, query):
    answer = []

    info_dict = make_info_dict(info)
    query_lists = get_query_list(query)

    for q in query_lists:
        q_key = q[0]
        q_score = q[1]
        count = 0
        if info_dict.get(q_key) is None:
            count = 0
        else:
            count = get_data_count(info_dict[q_key], q_score)
        answer.append(count)

    return answer


#1,1,1,1,2,4
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
               ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))