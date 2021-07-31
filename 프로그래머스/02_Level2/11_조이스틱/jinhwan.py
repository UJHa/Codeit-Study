def solution(name):
    answer = 0
    change = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    print(change)

    index = 0
    while True:
        answer += change[index]
        change[index] = 0
        if sum(change) == 0:
            break

        l, r = 1, 1
        #left
        while change[index - l] == 0:
            l += 1
        while change[index + r] == 0:
            r += 1

        answer += l if l < r else r
        index += -l if l < r else r

    return answer


# s = solution("JEROEN")
s = solution("JAN")
print(s)