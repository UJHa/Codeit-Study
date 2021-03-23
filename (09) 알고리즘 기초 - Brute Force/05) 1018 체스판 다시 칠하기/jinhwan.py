# (1018) 체스판 다시 칠하기
def redraw_count(board, pos_x, pos_y, start_color):
    wrong_count = 0

    correct_color = start_color

    # 입력받은 시작 좌표를 통해서 8x8 크기의 체스판의 각 칸 흑백 색깔 확인
    for y in range(pos_y, pos_y + 8):
        for x in range(pos_x, pos_x + 8):
            if board[y][x] != correct_color:
                wrong_count += 1

            # 가로(x 이동) 칸 이동 시 색을 번갈아서 체크
            correct_color = 'B' == correct_color and 'W' or 'B'

        # 세로(y 이동) 칸 이동 시 색을 번갈아서 체크
        correct_color = 'B' == correct_color and 'W' or 'B'

    return wrong_count


height, width = map(int,input().split())

chess_board = []
for i in range(height):
    chess_board.append(list(input()))

# 8x8의 체스판에서 최대 수정 값인 64로 비교를 해야 최소로 그리는 횟수를 알 수 있습니다.
min_value = 64
for start_pos_y in range(height - 7):
    for start_pos_x in range(width - 7):
        min_value = min(min_value,
                        redraw_count(chess_board, start_pos_x, start_pos_y, 'W'),
                        redraw_count(chess_board, start_pos_x, start_pos_y, 'B'))

print(min_value)