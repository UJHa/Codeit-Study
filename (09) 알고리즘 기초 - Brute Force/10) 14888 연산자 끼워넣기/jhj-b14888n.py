'''
max = 1000000001
min = -1000000001

반복문으로 연산( 횟수 n = k!/()()()() )
(연산자 문자열 리스트, 숫자리스트), 횟수 = 연산자 문자열 리스트 길이
연산자 문자열 길이 리스트 만들기: + - // * (0~n-1)
경우의 수는 재귀함수로 구하자(같은 연산자도 서로 다른으로 취급)
연산결과에 따라 max, min 바꿔주기

출력
'''

def insert_operator():

    n = int(input())
    list_num = list(map(int, input().split()))
    plus, minus, multiple, divide = map(int, input())
