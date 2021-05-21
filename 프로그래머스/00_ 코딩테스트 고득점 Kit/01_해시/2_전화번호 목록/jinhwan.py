# 1차 풀이 : 정확성 11,14번 실패, 효율성 성공
# 2차 풀이 : 정확성 성공, 효율성 4번 실패
def solution(phone_book):
    answer = True
    prefix_dict = {}

    for p in phone_book:
        if prefix_dict.get(len(p)) is None:
            prefix_dict[len(p)] = [p]
        else:
            prefix_dict[len(p)].append(p)

    for key, value in prefix_dict.items():
        num_length = key
        num_list = value
        for p in phone_book:
            if len(p) <= num_length:
                continue
            if p[:num_length] in num_list:
                return False

    return answer


print(solution(["119", "97674223", "1195524421"]))  # False
print(solution(["123", "456", "789"]))  # True
print(solution(["12", "123", "1235", "567", "88"]))  # False
