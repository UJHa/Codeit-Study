# 프린터(성공
# 정확성: 100.0
# 합계: 100.0 / 100.0
def solution(priorities, location):
    answer = 0
    temp_queue = []
    print_list = []

    # (순서, 중요도) 튜플로 temp_queue에 저장
    for i, p in enumerate(priorities):
        temp_queue.append((i, p))

    # temp_queue에서 하나씩 pop하면서 남은 리스트에서의 더 중요도 높은지 판별하여 print_list에 출력 순서대로 저장
    while len(temp_queue) != 0:
        tu = temp_queue.pop(0)
        # pop한 중요도보다 남은 리스트에 더 높은 수치가 최대값 중요도 존재 시
        if len(temp_queue) != 0 and tu[1] < max([i[1] for i in temp_queue]):
            temp_queue.append(tu)
        # pop 한 중요도가 출력 가능하면 print_list에 추가
        else:
            print_list.append(tu)

    # 저장된 print_list에서 location의 위치는 몇 번째로 실행되는지 확인
    for i, t in enumerate(print_list):
        if t[0] == location:
            answer = i + 1
            break

    return answer


s = solution([2, 1, 3, 2], 2)  # 1
print(s)
