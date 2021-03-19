'''
행,열 개수와 사탕 리스트 인풋
각 행의 좌표에 대해 1. 우측수 2.아래쪽 수 와 교환 시행(오른쪽으로 n-1번, 아래쪽으로 1번)
위 행동을 한번씩 내려오면서 (n-1)번 반복하면 모든 교환 케이스
교환 행동 할때마다 케이스 검사, 연속하는 개수 계산하여 이전 최대값과 교환
케이스검사(check max): 모든 좌표에 대해 상하로 검사 + 모든 좌표에 대해 좌우로 검사
최대값 반환
'''

import copy

def check_max(new_array, max_eatable):

    n = len(new_array)
    max_length = 0

    for i in range(n):  # (i, j) =(y, x)
        for j in range(n):

            length = 1
            updown_count = 1
            updown = [1, 1]
            while sum(updown) > 0:
                if updown[0] == 1:
                    if i - updown_count < 0:
                        updown[0] = 0
                    else:
                        if new_array[i - updown_count][j] == new_array[i][j]: length += 1
                        else: updown[0] = 0
                if updown[1] == 1:
                    if n - 1 < i + updown_count:
                        updown[1] = 0
                    else:
                        if new_array[i + updown_count][j] == new_array[i][j]: length += 1
                        else:updown[1] = 0
                updown_count += 1
            max_length = max(max_length, length)

            length = 1
            leftright_count = 1
            leftright = [1, 1]
            while sum(leftright) > 0:
                if leftright[0] == 1:
                    if j - leftright_count <0:
                        leftright[0] = 0
                    else:
                        if new_array[i][j - leftright_count] == new_array[i][j]: length += 1
                        else: leftright[0] = 0
                if leftright[1] == 1:
                    if n - 1 < j + leftright_count:
                        leftright[1] = 0
                    else:
                        if new_array[i][j + leftright_count] == new_array[i][j]: length += 1
                        else: leftright[0] = 0
                leftright_count += 1
            max_length = max(max_length, length)

    return max(max_eatable, max_length)

def candy_game():

    max_eatable = 0
    check_count = 0

    n = int(input())
    candy_array = [list(map(str, input())) for _ in range(n)]

    for i in range(n-1): # (i,j) == (y,x)
        for j in range(n):
            new_array = copy.deepcopy(candy_array)
            if j < n - 1: # 좌우 교환은 j가 우측 끝이 아닐 경우만
                new_array[i][j], new_array[i][j+1] = new_array[i][j+1], new_array[i][j]
                max_row = check_max(new_array, max_eatable)
                new_array[i][j], new_array[i][j + 1] = new_array[i][j + 1], new_array[i][j]

            new_array[i][j], new_array[i+1][j] = new_array[i+1][j], new_array[i][j]
            max_col = check_max(new_array, max_eatable)
            max_eatable = max(max_col, max_row)

    print(max_eatable)

    return 0

candy_game()