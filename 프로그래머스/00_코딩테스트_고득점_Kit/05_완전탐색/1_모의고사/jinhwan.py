# 모의고사(성공)
# 정확성: 100.0
# 합계: 100.0 / 100.0
def solution(answers):
    answer = []
    collect_count1 = 0
    collect_count2 = 0
    collect_count3 = 0

    select_list1 = [1, 2, 3, 4, 5]
    select_list2 = [2, 1, 2, 3, 2, 4, 2, 5]
    select_list3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i, a in enumerate(answers):
        # 1번 수포자
        if select_list1[i % len(select_list1)] == a:
            collect_count1 += 1
        # 2번 수포자
        if select_list2[i % len(select_list2)] == a:
            collect_count2 += 1
        # 3번 수포자
        if select_list3[i % len(select_list3)] == a:
            collect_count3 += 1

    max_count = max(collect_count1, collect_count2, collect_count3)
    if max_count == collect_count1:
        answer.append(1)
    if max_count == collect_count2:
        answer.append(2)
    if max_count == collect_count3:
        answer.append(3)
    return answer


# s = solution([1, 2, 3, 4, 5]) == [1]
s = solution([1, 3, 2, 4, 2]) == [1, 2, 3]
print(s)
