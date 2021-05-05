# 2차 풀이(정확도 100% 성공)
def solution(numbers, hand):
    answer = ''
    pos_num_dict = {}
    x, y = 0, 0
    for i in range(1, 12 + 1):
        if i == 10:
            pos_num_dict['*'] = [x, y]
        elif i == 11:
            pos_num_dict[0] = [x, y]
        elif i == 12:
            pos_num_dict['#'] = [x, y]
        else:
            pos_num_dict[i] = [x, y]

        x, y = (x + 1) % 3, i // 3

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