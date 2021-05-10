# 1차 풀이 실패(정확성 90%), 실패사유 : 시간 초과

from itertools import combinations


def get_course_count(orders, key):
    result = 0

    for order in orders:
        can_make_course = True

        for k in key:
            if k not in order:
                can_make_course = False
                break

        if can_make_course:
            result += 1

    return result


def solution(orders, course):
    answer = []
    alphabets = []

    for order in orders:
        for o in order:
            if o not in alphabets:
                alphabets.append(o)

    alphabets.sort()

    for c in course:
        max_count = 0
        course_list = []
        for tu in combinations(alphabets, c):
            key = ''.join(tu)
            course_count = get_course_count(orders, key)

            if max_count < course_count:
                course_list.clear()
                course_list.append(key)
                max_count = course_count
            elif max_count == course_count:
                course_list.append(key)

        if max_count > 1:
            answer += course_list

    answer.sort()

    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]) == ["AC", "ACDE", "BCFG", "CDE"])
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]) == ["ACD", "AD", "ADE", "CD", "XYZ"])
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]) == ["WX", "XY"])
