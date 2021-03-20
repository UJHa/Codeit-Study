# (2503) 숫자 야구
# 푸는 중...(아직 다 풀지 않는 문제)
n = int(input())
#3s, 1s 2b, 3b, 2s, 1s 1b, 0s 2b, 1s, 1b
for i in range(n):
    questions = list(map(int, input().split()))

all_numbers = {}
for i in range(1, 10):
    for j in range(1, 10):
        if i == j:
            continue
        for k in range(1, 10):
            if k == i or k == j:
                continue
            all_numbers[str(i)+str(j)+str(k)] = True

print(all_numbers)

for question in questions:
    question_number, strike, ball = str(question[0]), question[1], question[2]
    if strike + ball == 3:
        pass
    elif strike + ball == 2:
        pass
    elif strike + ball == 1:
        pass
    elif strike + ball == 0:
        pass

