# 정확성: 100.0
# 합계: 100.0 / 100.0
def solution(number, k):
    answer = ''
    start_index = 0
    while k > 0:
        max_index = start_index
        max_num = number[start_index]
        if start_index == len(number) - 1:
            break
        for i in range(start_index, start_index + k + 1):
            if max_num < number[i]:
                max_index = i
                max_num = number[i]
            if max_num == '9':
                break

        k -= max_index - start_index
        answer += max_num
        start_index = max_index + 1

    answer += number[start_index:]
    if k > 0:
        answer = answer[:-k]
    return answer


# s = solution("1924", 2)
s = solution("4177252841", 4)
# s = solution("52841", 1)
print(s)