# 1차 풀이 : 정확성 11,14번 실패, 효율성 성공
def solution(phone_book):
    answer = True
    length_list = []

    for p in phone_book:
        length_list.append(len(p))

    length_list = list(set(length_list))

    check_dict = {}
    for p in phone_book:
        for l in length_list:
            if len(p) < l:
                continue
            if check_dict.get(p[:l]) is None:
                check_dict[p[:l]] = 1
            elif check_dict[p[:l]] >= 1:
                check_dict[p[:l]] += 1

    for val in check_dict.values():
        if val > 1:
            return False

    return answer


print(solution(["119", "97674223", "1195524421"]))  # False
print(solution(["123", "456", "789"]))  # True
print(solution(["12", "123", "1235", "567", "88"]))  # False
