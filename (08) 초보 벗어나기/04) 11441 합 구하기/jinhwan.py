# 원소 개수 입력 받기
n = int(input())

# 이후 구간 입력에서 합 연산을 여러 번 하지 않도록
# 원소의 합으로 데이터 가공하여 array_list에 저장
array_list = [0]
sum_value = 0
for element in map(int, input().split()):
    sum_value += element
    array_list.append(sum_value)

# 구간 합 연산 몇 번 진행하는지 정하는 입력 받기
input_time = int(input())
result_list = []

# 합 연산된 리스트에서 제외 되는 구간의 차로 합한 결과 저장
for index in range(input_time):
    x, y = map(int, input().split())

    result_list.append(array_list[y] - array_list[x-1])

# 결과 출력
for num in result_list:
    print(num)