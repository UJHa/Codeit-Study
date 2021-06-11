# 가장 큰 수(실패)
# 정확성: 27.3
# 합계: 27.3 / 100.0
import heapq


def solution(numbers):
    answer = ''
    max_number_length = 4 # 1000
    num_heap = []
    for n in numbers:
        compare_num = -n * 10 ** (max_number_length - len(str(n)))
        heapq.heappush(num_heap, (compare_num, n))

    while num_heap:
        num = heapq.heappop(num_heap)[1]
        answer += str(num)
    return answer

# 2 * (i + 1) - 1, 2 * (i + 1)

s = solution([6, 10, 2])  # "6210"
print(s)