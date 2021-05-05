# 2차 풀이(정확도 100% 성공)
def solution(numbers, hand):
    answer = ''
    # for문 없이 직접 12개 키패드 좌표 지정
    pos_num_dict = {1: (0, 0), 2: (1, 0), 3: (2, 0),
                    4: (0, 1), 5: (1, 1), 6: (2, 1),
                    7: (0, 2), 8: (1, 2), 9: (2, 2),
                    '*': (0, 3), 0: (1, 3), '#': (2, 3)
                    }

    left_pos = pos_num_dict['*']
    right_pos = pos_num_dict['#']

    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            left_pos = pos_num_dict[n]
        elif n in [3, 6, 9]:
            # 369 right
            answer += 'R'
            right_pos = pos_num_dict[n]
        else:  # 2, 5, 8, 0
            # 2580 조건
            center_pos = pos_num_dict[n]
            left_distance = abs(center_pos[0] - left_pos[0]) + abs(center_pos[1] - left_pos[1])
            right_distance = abs(center_pos[0] - right_pos[0]) + abs(center_pos[1] - right_pos[1])
            if left_distance < right_distance:
                answer += 'L'
                left_pos = center_pos
            elif left_distance > right_distance:
                answer += 'R'
                right_pos = center_pos
            else:
                if hand == 'left':
                    answer += 'L'
                    left_pos = center_pos
                elif hand == 'right':
                    answer += 'R'
                    right_pos = center_pos

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
