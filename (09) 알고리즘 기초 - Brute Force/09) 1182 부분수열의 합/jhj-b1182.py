# 풀이
# 정수 개수 n 받음

# 1~2**n까지 이진수로 변환
# 스트링 리스트 형태로 저장
# 반환

# list[i][n-j-1,n]에 대해 해당하는 원소를 text_list에 저장 후 sum 구하고 비교
# 같으면 count += 1

def section_sequence_generator(n):

    case_list = []
    for i in range(1, 2**n):
        added_digit = n
        num_binary = ''
        while i > 0:
            if i % 2 == 1:
                num_binary = '1' + num_binary
            else: num_binary = '0' + num_binary
            i = i//2
            added_digit -= 1
        num_binary = '0'*added_digit +num_binary
        case_list.append(num_binary)
    return case_list

def sum_section_sequence():

    n, s = map(int, input().split())
    sequence_list = list(map(int, input().split()))
    section_sequence_list = section_sequence_generator(n)

    count = 0

    for num in section_sequence_list:
        test_list =[]
        for j in range(n):
            if num[j] == '1':test_list.append(sequence_list[j])
        if sum(test_list) == s: count += 1

    print(count)

    return 0

sum_section_sequence()
