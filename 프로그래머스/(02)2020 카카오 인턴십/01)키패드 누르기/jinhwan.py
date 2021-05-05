# 1차 풀이(정확도 60%로 실패)
def get_num_pos(pos_num_list, number):
    for y in range(len(pos_num_list)):
        for x in range(len(pos_num_list[y])):
            if number == pos_num_list[y][x]:
                return [x, y]
    return None


def solution(numbers, hand):
    answer = ''
    pos_num_list = []
    pos_num_list.append(['1', '2', '3'])
    pos_num_list.append(['4', '5', '6'])
    pos_num_list.append(['7', '8', '9'])
    pos_num_list.append(['*', '0', '#'])

    left_hand_pos = get_num_pos(pos_num_list, '*')
    right_hand_pos = get_num_pos(pos_num_list, '#')

    for n in numbers:
        n = str(n)
        if n in ['1', '4', '7']:
            answer += 'L'
            left_hand_pos = get_num_pos(pos_num_list, n)
            pass
        elif n in ['3', '6', '9']:
            # 369 right
            answer += 'R'
            right_hand_pos = get_num_pos(pos_num_list, n)
            pass
        else:  # 2, 5, 8, 0
            # 2580 조건
            center_pos = get_num_pos(pos_num_list, n)
            left_distance = (center_pos[0] - left_hand_pos[0]) ** 2 + (center_pos[1] - left_hand_pos[1]) ** 2
            right_distance = (center_pos[0] - right_hand_pos[0]) ** 2 + (center_pos[1] - right_hand_pos[1]) ** 2
            if left_distance < right_distance:
                answer += 'L'
                left_hand_pos = center_pos
            elif left_distance > right_distance:
                answer += 'R'
                right_hand_pos = center_pos
            else:
                if hand == 'left':
                    answer += 'L'
                    left_hand_pos = center_pos
                elif hand == 'right':
                    answer += 'R'
                    right_hand_pos = center_pos

    return answer