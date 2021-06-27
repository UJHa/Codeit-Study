# 모의고사
def solution(answers):
    answer = []
    select_list1 = [1, 2, 3, 4, 5]
    select_list2 = [2, 1, 2, 3, 2, 4, 2, 5]
    select_list3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    students = [0, 0, 0]
    for i, a in enumerate(answers):
        if a == select_list1[i % len(select_list1)]:
            students[0] += 1
        if a == select_list2[i % len(select_list2)]:
            students[1] += 1
        if a == select_list3[i % len(select_list3)]:
            students[2] += 1
    max_count = max(students)
    for i, s in enumerate(students):
        if s == max_count:
            answer.append(i + 1)

    return answer


# s = solution([1,2,3,4,5]) == [1]
s = solution([1,3,2,4,2]) == [1,2,3]
print(s)