def solution(gems):
    answer = [0, len(gems)]

    check_dict = {gems[0]: 1}

    gem_count = len(set(gems))

    left, right = 0, 0
    while left < len(gems) and right < len(gems):
        if len(check_dict) == gem_count:
            if right - left < answer[1] - answer[0]:
                answer = [left+1, right+1]

            if check_dict[gems[left]] == 1:
                del check_dict[gems[left]]
            else:
                check_dict[gems[left]] -= 1

            left += 1
        else:
            right += 1
            if right == len(gems):
                break

            if check_dict.get(gems[right]) is None:
                check_dict[gems[right]] = 1
            else:
                check_dict[gems[right]] += 1

    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))