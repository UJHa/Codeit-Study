# 1차 풀이(성공)
import itertools


def solution(expression):
    split_datas = []

    prev_end = 0
    for i, ch in enumerate(expression):
        if ch in ['+', '*', '-']:
            split_datas.append(int(expression[prev_end:i]))
            split_datas.append(ch)
            prev_end = i + 1
    split_datas.append(int(expression[prev_end:]))

    max_reward = 0
    # 각 경우의 수들에 대한 반복문
    for order_list in itertools.permutations(['+', '*', '-'], 3):
        temp_list = list(split_datas)
        # 연산자 +, *, -의 우선순위 연산부터 실행하는 반복문
        for operator in order_list:
            # 하나의 연산자에 대한 처리를 진행하는 반복문
            while operator in temp_list:
                op_index = temp_list.index(operator)
                if operator == '+':
                    temp_list[op_index - 1] = temp_list[op_index - 1] + temp_list[op_index + 1]
                elif operator == '*':
                    temp_list[op_index - 1] = temp_list[op_index - 1] * temp_list[op_index + 1]
                elif operator == '-':
                    temp_list[op_index - 1] = temp_list[op_index - 1] - temp_list[op_index + 1]

                del temp_list[op_index:op_index + 2]
        max_reward = max(max_reward, abs(temp_list[0]))

    return max_reward


print('answer', solution("100-200*300-500+20"))