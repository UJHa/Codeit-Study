# 1차 풀이 성공(정확성 100%)
# 1차 풀이 : 모든 문자 리스트 생성 후 그에 대한 경우의 수별로 최대의 코스를 반환
# 2차 풀이 : orders에 들어 있는 코스에 대해서만 경우의 수를 key로 개수를 value로 해서 2개 이상인 코스들을 반환
from itertools import combinations


def solution(orders, course):
    answer = []

    course_dict = {}
    for order in orders:
        for c in course:
            for tu in combinations(order, c):
                key = ''.join(sorted(tu))
                if course_dict.get(key) is None:
                    course_dict[key] = 1
                else:
                    course_dict[key] += 1

    for c in course:
        max_count = 0
        course_list = []
        for k, v in course_dict.items():
            if c == len(k):
                if max_count < v:
                    course_list = [k]
                    max_count = v
                elif max_count == v:
                    course_list.append(k)
        if max_count > 1:
            answer += course_list

    for i, val in enumerate(answer):
        alphabet_list = list(val)
        alphabet_list.sort()
        answer[i] = ''.join(alphabet_list)

    answer.sort()

    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]) == ["AC", "ACDE", "BCFG", "CDE"])
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]) == ["ACD", "AD", "ADE", "CD", "XYZ"])
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]) == ["WX", "XY"])