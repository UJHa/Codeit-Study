# (1018) 체스판 다시 칠하기
# 푸는 중...(아직 오답)
def redraw_count(board, pos_x, pos_y):
    wrong_count = 0

    start_color = board[pos_y][pos_x]
    correct_color = start_color

    for y in range(pos_y, pos_y + 8):
        for x in range(pos_x, pos_x + 8):
            if board[y][x] != correct_color:
                wrong_count += 1

            correct_color = 'B' == correct_color and 'W' or 'B'

        start_color = 'W' == start_color and 'B' or 'W'
        correct_color = start_color

    return wrong_count


height, width = map(int,input().split())

chess_board = []
for i in range(height):
    chess_board.append(list(input()))

min_value = 64
for start_pos_y in range(height - 7):
    for start_pos_x in range(width - 7):
        min_value = min(min_value, redraw_count(chess_board, start_pos_x, start_pos_y))

print(min_value)