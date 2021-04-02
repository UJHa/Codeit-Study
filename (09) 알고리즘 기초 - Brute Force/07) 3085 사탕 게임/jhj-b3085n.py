'''
행,열 개수와 사탕 리스트 인풋
serial_max = 0 으로 초기화
각 좌표마다 check changed(for문 2번) (해당 문자에 대해서만 체크)(오른쪽, 아래쪽과 바꾼 경우만 체크하기)
check changed로 바꾼 경우에 대해 연속한 사탕 최대 개수 출력하고 기존 serial_max와 비교
serial max 반환
'''

import copy

def check_changed_board(board, y, x):
    color = board(y, x)
    changed_board_row = copy.deepcopy(board)
    changed_board_col = copy.deepcopy(board)
    up_tag = 0
    down_tag = 0
    count_updown = 1
    serial_max_updown = 1

    right_tag = 0
    left_tag = 0
    count_updown = 1
    serial_max_updown = 1

    check_changed = 0

    while up_tag*down_tag == 0:
        if y - count_updown < 0:
            up_tag = 1
        else:
            if color != changed_board_col[y-count_updown][x]:









def bomboni():

    serial_max = 0
    n = int(input())
    board = [list(map(str, input())) for _ in range(n)]

    for y in range(n - 1): # 1~n-1열까지 아래랑 교체
        for x in range(n - 1): # 1~n-1행까지 오른쪽과 교체
            serial_max = max(serial_max, check_changed_board(board, y, x))

bomboni()