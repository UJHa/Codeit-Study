# 키패드 누르기
# 06-21 11:58~12:19(약 20분)
# 정확성: 100.0
# 합계: 100.0 / 100.0
def solution(numbers, hand):
    answer = ''
    numpad_dict = {1: (0, 0), 2: (1, 0), 3: (2, 0),
                   4: (0, 1), 5: (1, 1), 6: (2, 1),
                   7: (0, 2), 8: (1, 2), 9: (2, 2),
                   '*':(0, 3), 0: (1, 3), '#': (2, 3)}
    cur_left_hand = numpad_dict['*']
    cur_right_hand = numpad_dict['#']
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            cur_left_hand = numpad_dict[num]
        elif num in [3, 6, 9]:
            answer += 'R'
            cur_right_hand = numpad_dict[num]
        else: # 2, 5, 8, 0
            left_move_x = abs(cur_left_hand[0] - numpad_dict[num][0])
            left_move_y = abs(cur_left_hand[1] - numpad_dict[num][1])
            right_move_x = abs(cur_right_hand[0] - numpad_dict[num][0])
            right_move_y = abs(cur_right_hand[1] - numpad_dict[num][1])
            left_move = left_move_x + left_move_y
            right_move = right_move_x + right_move_y
            if left_move < right_move or (left_move == right_move and hand == 'left'):
                answer += 'L'
                cur_left_hand = numpad_dict[num]
            elif left_move > right_move or (left_move == right_move and hand == 'right'):
                answer += 'R'
                cur_right_hand = numpad_dict[num]

    return answer


s = solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") == "LRLLLRLLRRL"
print(s)
