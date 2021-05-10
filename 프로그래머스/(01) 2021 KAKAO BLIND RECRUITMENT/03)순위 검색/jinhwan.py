# 4차 성공(정확성은 100%, 효율성 100%)
# 1차 방식 : info 데이터 내부의 columns 하나씩 비교하는 방식
# 2차 방식 : info의 column들을 가져와서 일치하는 데이터의 index에 접근하여 비교하는 방식
# 3차 방식 : info의 점수를 뺀 나머지 데이터를 문자열 키로 dictionary 생성, query로 key를 만들어서 dict의 value(list)에서 점수가 query score이상인 갯수 반환 방식
# 4차 방식
# # 정렬(sort)를 query 실행 시점이 아니라 info_dict 생성 후 실행하도록 변경(query 배열의 최대 크기보다 info 배열의 최대 크기가 작음)
# # 점수 조건에 일치하는 개수를 이진 탐색(lower bound)으로 변경

from itertools import combinations
from bisect import bisect_left


def make_info_dict(info):
    result = {}
    for _i in info:
        val = _i.split()
        score = int(val[-1])
        data = val[:-1]

        for num in range(5):
            for tu in combinations([0, 1, 2, 3], num):
                key_string = make_info_key_string(data, tu)

                if result.get(key_string) is None:
                    result[key_string] = [score]
                else:
                    result[key_string].append(score)
    return result


def make_info_key_string(data, combine_tuple):
    result = ''
    for i in range(4):
        if i in combine_tuple:
            result += '-'
        else:
            result += data[i]
    return result


def solution(info, query):
    answer = []

    info_dict = make_info_dict(info)

    for val in info_dict.values():
        val.sort()

    for q in query:
        q_data = q.split()
        q_key = q_data[0] + q_data[2] + q_data[4] + q_data[6]
        q_score = int(q_data[-1])

        if info_dict.get(q_key) is None:
            count = 0
        else:
            data_list = info_dict[q_key]
            count = len(data_list) - bisect_left(data_list, q_score)
        answer.append(count)

    return answer


#1,1,1,1,2,4
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
               ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))