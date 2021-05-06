import operator


class Tile:
    def __init__(self, cur_pos, prev_pos, cost):
        self.cur_pos = cur_pos
        self.prev_pos = prev_pos
        self.cost = cost


def get_next_position(pos, direction, length):
    next_pos = [pos[0] + direction[0], pos[1] + direction[1]]
    if 0 <= next_pos[0] < length and 0 <= next_pos[1] < length:
        return next_pos
    else:
        return None


# 3에서 25까지의 N 범위는 최대숫자 길이가 N이므로 x, y 좌표를 0000포맷의 문자열로 변환해서 사용
def get_pos_to_str(pos):
    result = ''
    if pos[0] < 10:
        result += '0'+str(pos[0])
    else:
        result += str(pos[0])
    if pos[1] < 10:
        result += '0' + str(pos[1])
    else:
        result += str(pos[1])
    return result


def solution(board):
    answer = 0
    N = len(board)

    queue = []
    start_pos = [0, 0]
    end_pos = [N - 1, N - 1]
    # 키를 x,y좌표, value를 이전 위치와 현재 경로까지의 비용을 묶은 Tile 클래스로 저장
    board_dict = {get_pos_to_str(start_pos):Tile(start_pos, None, 0)}
    # 하, 우, 상, 좌 순서로 방향 list 저장
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    queue.append(board_dict[get_pos_to_str(start_pos)])
    while queue:
        queue.sort(key=operator.attrgetter('cost'))
        tile = queue.pop(0)
        # print(tile.cur_pos, tile.prev_pos, tile.cost)
        if tile.cur_pos[0] == end_pos[0] and tile.cur_pos[1] == end_pos[1]:
            break
        for d in directions:
            # NxN 벗어나지 않는 next_pos 구하기
            next_pos = get_next_position(tile.cur_pos, d, N)
            # 탐색 가능한 next_pos인 경우(next_pos가 NxN 범위 안이고 벽이 아닐 경우)
            if next_pos is not None and board[next_pos[1]][next_pos[0]] != 1:
                # 다음 타일이 직선 도로/코너에 따라 비용 설정
                cost = 0
                if tile.prev_pos is None:
                    cost = 100
                elif tile.prev_pos[0] == tile.cur_pos[0] == next_pos[0] \
                        or tile.prev_pos[1] == tile.cur_pos[1] == next_pos[1]:
                    cost = 100
                else:
                    cost = 100 + 500

                # board_dict가 없을 때 좌표를 key, tile 클래스를 value로 저장
                key_pos = get_pos_to_str(next_pos)
                if board_dict.get(key_pos) is None:
                    queue.append(Tile(next_pos, tile.cur_pos, tile.cost + cost))
                    board_dict[key_pos] = Tile(next_pos, tile.cur_pos, tile.cost + cost)
                # board_dict의 key가 있을 때
                else:
                    # 기존 타일까지의 비용이 더 쌀 때 그대로 저장
                    if board_dict[key_pos].cost <= tile.cost + cost:
                        # print('비용 그대로 : ', key_pos , board_dict[key_pos].cost, tile.cost + cost)
                        pass
                    # 현재 설정한 next_pos의 비용이 더 쌀 때 value를 변경하여 저장
                    else:
                        # print('비용 전환 : ', key_pos, board_dict[key_pos].cost, tile.cost + cost)
                        board_dict[key_pos] = Tile(next_pos, tile.cur_pos, tile.cost + cost)

    # print(board_dict[get_pos_to_str(end_pos)])

    return board_dict[get_pos_to_str(end_pos)].cost


print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))