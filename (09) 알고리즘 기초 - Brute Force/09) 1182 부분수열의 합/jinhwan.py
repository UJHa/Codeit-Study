# (1182) 부분수열의 합
def sum_check(seq_list, sum_value):
    total_count = 0

    # n개로 만들 수 있는 부분 수열의 총 개수 : (2**n) 개
    for i in range(1, 2 ** len(seq_list)):
        bin_check = bin(i)[2:]

        # 다섯 자리의 이진 문자열로 변환(예 : 00001, 01010)
        for j in range(len(seq_list) - len(bin_check)):
            bin_check = '0' + str(bin_check)

        # print(f'{bin_check}, {i}')

        # 이진 문자열(예 : 00001, 01010)은
        # # 1을 부분 수열로 포함
        # # 0을 부분 수열로 미포함
        # # 0,1 두 숫자를 통하여 모든 부분 수열을 구할 수 있습니다.
        temp_sum = 0
        for index in range(len(bin_check)):
            temp_sum += int(bin_check[index]) * seq_list[index]

        # 요구하는 S와 같은 합이 나올 경우 출력값(total_count) 증가
        if temp_sum == sum_value:
            total_count += 1

    return total_count


N, S = map(int, input().split())

sequence = list(map(int, input().split()))
print(sum_check(sequence, S))
