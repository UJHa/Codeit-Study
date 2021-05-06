import math


def solution(board):
    answer = 0
    N = len(board)

    start_pos = (0, 0)
    # 하, 우, 상, 좌 순서로 방향 list 저장
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def get_cost(start_data):
        cost_table = [[math.inf for _ in range(N)] for _ in range(N)]

        queue = [start_data]
        cost_table[0][0] = 0
        while queue:
            (x, y), direction, cost = queue.pop(0)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                d = (dx, dy)
                next_pos = (nx, ny)

                cal_cost = 0
                if direction == d:
                    cal_cost = cost + 100
                else:
                    cal_cost = cost + 100 + 500

                if 0 <= nx < N and 0 <= ny < N and board[ny][nx] == 0 and cal_cost < cost_table[ny][nx]:
                    cost_table[ny][nx] = cal_cost
                    queue.append([next_pos, d, cal_cost])

        return cost_table[N-1][N-1]

    answer = min(get_cost([start_pos, directions[0], 0]),
                 get_cost([start_pos, directions[1], 0]))

    return answer


print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))