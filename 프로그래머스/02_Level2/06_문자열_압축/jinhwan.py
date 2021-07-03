# 문자열 압축
def solution(s):
    answer = len(s)

    for i in range(1, len(s) // 2 + 1):
        zip_str, count = '', 1
        temp = s[:i]

        for j in range(i, len(s), i):
            cur_str = s[j:j+i]
            if temp == cur_str:
                count += 1
            else:
                if count > 1:
                    zip_str += str(count)
                zip_str += temp
                temp = cur_str
                count = 1

        if count > 1:
            zip_str += str(count)
        zip_str += temp

        if answer > len(zip_str):
            answer = len(zip_str)

    return answer


s = solution('aabbaccc') == 7
print(s)