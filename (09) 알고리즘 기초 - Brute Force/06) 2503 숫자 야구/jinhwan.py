# (2503) 숫자 야구
# ljh.py 참고했습니다.
def check_strike(question_num, temp_num):
    result = 0
    for i in range(3):
        if question_num[i] == temp_num[i]:
            result += 1
    return result


def check_ball(question_num, temp_num):
    result = 0

    if question_num[0] == temp_num[1] or question_num[0] == temp_num[2]: result += 1
    if question_num[1] == temp_num[2] or question_num[1] == temp_num[0]: result += 1
    if question_num[2] == temp_num[0] or question_num[2] == temp_num[1]: result += 1

    return result


n = int(input())

questions = []
for i in range(n):
    questions.append(list(map(int, input().split())))

all_numbers = {}
for i in range(1, 10):
    for j in range(1, 10):
        if i == j:
            continue
        for k in range(1, 10):
            if k == i or k == j:
                continue
            all_numbers[str(i)+str(j)+str(k)] = True

for question in questions:
    question_number, strike, ball = str(question[0]), question[1], question[2]
    for num in all_numbers:
        s = check_strike(question_number, num)
        b = check_ball(question_number, num)
        if s != strike or b != ball:
            all_numbers[num] = False

output_value = 0
for key, val in all_numbers.items():
    if val == True:
        output_value += 1

print(output_value)

