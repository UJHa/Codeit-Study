# 게임맵 최단거리
from collections import deque


def solution(maps):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x_len, y_len = len(maps[0]), len(maps)
    moved_list = [[-1 for _ in range(x_len)] for _ in range(y_len)]

    queue = deque()
    queue.append((0, 0))
    moved_list[0][0] = 1
    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            mx, my = x + dx, y + dy
            if 0 <= mx < x_len and 0 <= my < y_len:
                if maps[my][mx] == 1 and moved_list[my][mx] == -1:
                    moved_list[my][mx] = moved_list[y][x] + 1
                    queue.append((mx, my))

    answer = moved_list[-1][-1]
    return answer


s = solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]) == 11
# s = solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]) == -1
print(s)
