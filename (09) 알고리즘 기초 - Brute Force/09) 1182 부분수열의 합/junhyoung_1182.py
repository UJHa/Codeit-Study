# 부분수열의 합
import copy


def partical_sequence(n, want_sum, sequence):
    count = 0
    # num : 리스트 원소중 몇개를 선택해 부분 수열을 만들건지
    for num in range(1, len(sequence)+1):
        current = sum_partical(num, sequence)
        count += current.count(want_sum)
    return count


# sequence 로 부터 부분수열을 만든다.
# n개로 이루어져 있고, 그 부분수열의 합을 리턴해준다
def sum_partical(n, sequence):
    if n == 1:
        return sequence

    # 부분수열의 합
    sum_list = []
    # n >= 2 인 상황
    # i 는 sequence 의 원소중 하나 선택
    for i in range(len(sequence)-n+1):
        temp = copy.deepcopy(sequence)
        cut = sum_partical(n-1, temp[i+1:])
        for j in range(len(cut)):
            cut[j] += temp[i]
            sum_list.append(cut[j])

    return sum_list


num, my_want_sum = map(int, input().split())
my_sequence = list(map(int, input().split()))

print(partical_sequence(num, my_want_sum, my_sequence))
