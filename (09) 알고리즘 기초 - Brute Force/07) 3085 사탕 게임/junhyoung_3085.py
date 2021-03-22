# 사탕 게임

# 한칸씩 위, 오른쪽, 아래, 왼쪽과 바꾸어 연속되는 같은 색상의 사탕의 개수를 찾는다.
# 가장 많은 수를 리턴
import copy

def candy(n, board):
    max_count = 0
    for i in range(n):
        for j in range(n):
            # 위, 오른쪽, 아래, 왼쪽과 바꾼다
            for k in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                current = copy.deepcopy(board)
                # 이차원 배열을 벗어났을 경우
                if i+k[0] < 0 or i+k[0] > n-1 or j+k[1] < 0 or j+k[1] > n-1:
                    continue
                current[i][j], current[i+k[0]][j+k[1]] = current[i+k[0]][j+k[1]], current[i][j]
                max_count = max(eating_count(current, i, j), max_count)
                # 원래 상태로 복구
                #current[i][j], current[i + k[0]][j + k[1]] = current[i + k[0]][j + k[1]], current[i][j]
    return max_count


def eating_count(board, row, col):
    left = 0
    right = 0
    up = 0
    down = 0

    # 왼쪽으로 한칸씩 이동하며 같은 색상인지 판단
    # 다른 색상이면 반복문 탈출
    for i in range(1, row+1):
        if board[row - i][col] == board[row][col]:
            left += 1
        else:
            break
    # 오른쪽
    for i in range(1, len(board)-row):
        if board[row + i][col] == board[row][col]:
            right += 1
        else:
            break
    # 위
    for i in range(1, col+1):
        if board[row][col - i] == board[row][col]:
            up += 1
        else:
            break
    # 아래
    for i in range(1, len(board)-col):
        if board[row][col + i] == board[row][col]:
            down += 1
        else:
            break

    # 자신을 포함해야 총 개수가 나와 +1을 해줌
    return max(left+right+1, up+down+1)


size = int(input())
my_board = [[0]*size for _ in range(size)]
for i in range(size):
    temp = input()
    for j in range(len(temp)):
        my_board[i][j] = temp[j]


print(candy(size, my_board))
