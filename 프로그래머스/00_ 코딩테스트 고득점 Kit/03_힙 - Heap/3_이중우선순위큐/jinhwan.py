# 이중우선순위큐(성공)(테스트 케이스로 불충분, ["I 2","I 4","D -1", "I 1", "D 1"] 테스트도 필요)
# 정확성: 100.0
# 합계: 100.0 / 100.0
import heapq


def solution(operations):
    answer = []
    num_dict = {}
    min_heap_queue = []
    max_heap_queue = []
    key_index = 0

    for o in operations:
        command, num = o.split()
        num = int(num)
        if command == 'I':
            num_dict[key_index] = num
            heapq.heappush(min_heap_queue, (num, key_index))
            heapq.heappush(max_heap_queue, (-1 * num, key_index))
            key_index += 1
        elif command == 'D' and num == 1:
            if max_heap_queue:
                value, key = heapq.heappop(max_heap_queue)
                if num_dict.get(key):
                    num_dict.pop(key)
                    min_heap_queue = [(v, k) for k, v in num_dict.items()]
                    heapq.heapify(min_heap_queue)
        elif command == 'D' and num == -1:
            if min_heap_queue:
                value, key = heapq.heappop(min_heap_queue)
                if num_dict.get(key):
                    num_dict.pop(key)
                    max_heap_queue = [(-v, k) for k, v in num_dict.items()]
                    heapq.heapify(max_heap_queue)

    if num_dict:
        if len(num_dict.values()) == 1:
            answer = list(num_dict.values()) * 2
        else:
            max_value = - heapq.heappop(max_heap_queue)[0]
            min_value = heapq.heappop(min_heap_queue)[0]
            answer = [max_value, min_value]
    else:
        answer = [0, 0]

    return answer


# s = solution(["I 16", "D 1"])  # [0,0]
# s = solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])  # [0, 0]
# s = solution(["I 7","I 5","I -5","D -1"])  # [7,5]
s = solution(["I 2","I 4","D -1", "I 1", "D 1"])  # [1, 1]
print(s)
