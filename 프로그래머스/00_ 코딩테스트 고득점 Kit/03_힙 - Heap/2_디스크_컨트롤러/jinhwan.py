# 디스크 컨트롤러(성공)
# 매 초 단위의 검사 방식
# 정확성: 100.0
# 합계: 100.0 / 100.0
import heapq


def solution(jobs):
    answer = 0

    heap_list = []

    start, now, i = -1, 0, 0
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap_list, (j[1], j[0]))
        if heap_list:
            process_time, request_time = heapq.heappop(heap_list)
            start = now
            end_work_time = now + process_time
            answer += end_work_time - request_time
            now = end_work_time
            i += 1
        else:
            now += 1

    return answer // len(jobs)


s = solution([[0, 3], [1, 9], [2, 6]])  # 9
print(s)
