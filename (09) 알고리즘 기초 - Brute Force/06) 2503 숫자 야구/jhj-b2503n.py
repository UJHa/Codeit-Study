'''
자리수별로 가능한 숫자 리스트 생성
볼과 스트라이크 개수에 따라 숫자 추가
case
3s 0b 0o
2s 0b 1o
1s 0b 0o
1s 1b 1o
1s 2b 0o
0s 0b 3o
0s 1b 2o
0s 2b 1o
0s 3b 0o
개능한 개수 출력
'''

def write_list(answer_list, x, strike, ball):

    a = x//100
    b = x//10
    c = x % 10

    if strike == 0:
        if ball == 3:
            answer_list[0].append


def guess_answer_case():

    n = int(input())
    answer_list = [[],[],[]]

    for i in range(n):
        x, strike, ball = map(int, input().split())

    print(len(answer_list[0])*len(answer_list[1])*len(answer_list[2]))

    return 0


guess_answer_case()