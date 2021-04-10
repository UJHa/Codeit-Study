# (1003) 피보나치 함수
fibo_dict = {}


def fibonacci(n):
    if n == 0:
        if fibo_dict.get(n) is None:
            fibo_dict[n] = 0
        return fibo_dict[n]
    elif n == 1:
        if fibo_dict.get(n) is None:
            fibo_dict[n] = 1
        return fibo_dict[n]
    else:
        if fibo_dict.get(n) is None:
            fibo_dict[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return fibo_dict[n]


# 입력에 대한 처리
n = int(input())

test_cases = []
for i in range(n):
    test_cases.append(int(input()))

for test_num in test_cases:
    if test_num == 0:
        print('1 0')
    elif test_num == 1:
        print('0 1')
    else:
        fibo_number = fibonacci(test_num)
        print(f'{fibonacci(test_num - 1)} {fibonacci(test_num)}')