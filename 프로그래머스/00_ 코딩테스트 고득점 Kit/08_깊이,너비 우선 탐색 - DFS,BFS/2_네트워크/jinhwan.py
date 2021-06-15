# 네트워크(성공)
# 정확성: 100.0
# 합계: 100.0 / 100.0
from collections import deque


def solution(n, computers):
    answer = 0
    remain_list = [i for i in range(n)]

    # 모든 컴퓨터가 remain_list에서 제외될 때까지 반복
    while len(remain_list) > 0:
        find_queue = deque()

        # remain_list 길이가 0보다 크면 매번 0번 인덱스가 존재함
        # find_queue를 실행하기 위해 remain_list[0]을 삽입
        find_queue.append(remain_list[0])
        while len(find_queue) > 0:
            # 들어있는 큐에서 순차적으로 pop하기(0번 인덱스)
            c_index = find_queue.pop()
            # 연결되어 있는 다른 컴퓨터에서 pop으로 제거했을 수도 있으므로 remain_list에 있는지 확인 조건 필요
            if c_index in remain_list:
                remain_list.remove(c_index)
            for i, connect in enumerate(computers[c_index]):
                if i == c_index:
                    continue
                elif connect == 1 and i in remain_list:
                    # 연결되어 있고, remain_list에 남아 있는 컴퓨터만 큐에 넣음
                    find_queue.append(i)
        answer += 1

    return answer


# s = solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])  # 2
# s = solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])  # 1
s = solution(1, [[1]])  # 1
print(s)
