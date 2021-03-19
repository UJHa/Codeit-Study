'''
max = 1000000001
min = -1000000001

반복문으로 연산( 횟수 n = k!/()()()() )
경우의 수는 재귀함수로 구하자(같은 연산자도 서로 다른으로 취급)
연산결과에 따라 max, min 바꿔주기

출력
'''

def calc_operate_case(n, plus, minus, mult, divd, operate_case):

    if n == 1:
        if plus == 1: return ['+']
        elif minus == 1: return ['-']
        elif mult == 1: return ['x']
        else: return ['//']

    else:
        for i in operate_case:
            for j in range



def insert_operator():

    max = -1000000001
    min = 1000000001

    n = int(input())
    num_list = list(map(int, input().split()))
    plus, minus, mult, divd = map(int, input().split()) # 더하기 빼기 곱하기 나누기 개수

    operate_case = []

    for i in range(1,n)

    for i in range()







insrt_operator()