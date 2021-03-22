# 체스판 다시 칠하기

# 입력받은 체스 상태를 이차원 배열로 바꿔준다
# 8*8로 자른판에서 몇개의 칸을 다시 칠할지 최소의 개수를 구한다
# shape = (x, y), board : 체스판 상태
def painting_chess(shape, board):
    min_painting = None
    for i in range(shape[0]-8+1):
        for j in range(shape[1]-8+1):
            # 8*8로 자름
            cut_board = [[board[row][col] for col in range(j, j+8)] for row in range(i, i+8)]

            # 8*8을 처음으로 잘랐을 경우
            if min_painting is None:
                min_painting = change_color(cut_board)

            # 가장 최소의 개수를 저장
            min_painting = min(min_painting, change_color(cut_board))

    return min_painting

# 8*8로 자른판에서
# 1. 검은색부터 칠했을 경우
# 2. 흰색부터 칠했을 경우 몇개의 칸을 다시 칠할지 알려준다.
# 둘 중 최소의 개수를 리턴
def change_color(board):
    start_white = 0
    start_black = 0
    # 맨 왼쪽이 흰색, 검은색으로 칠할때 각각 비교해주기 위한 리스트
    # compare[1] = 'W', compare[-1] = 'B'
    compare = [' ', 'W', 'B']
    compare_index = 1

    for i in range(8):
        for j in range(8):
            # 맨 왼쪽이 흰색으로 시작할 경우
            if board[i][j] != compare[compare_index]:
                start_white += 1

            # 맨 왼쪽이 검은색으로 시작할 경우
            if board[i][j] != compare[compare_index * (-1)]:
                start_black += 1

            # 열이 바뀔때 비교할 색을 바꿔줌
            compare_index *= -1

        # 행이 바뀔때 비교할 색을 바꿔줌
        compare_index *= -1

    # print(start_white, start_black)
    count = min(start_white, start_black)

    return count


my_shape = list(map(int, input().split()))
# (행의 개수, 열의 개수)인 이차원 배열 초기화
my_board = [[-1]*my_shape[1] for _ in range(my_shape[0])]

# 입력받은 체스 상태를 my_chess 에 값을 할당
for i in range(my_shape[0]):
    temp = input()
    for j in range(my_shape[1]):
        my_board[i][j] = temp[j]

print(painting_chess(my_shape, my_board))



