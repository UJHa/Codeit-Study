# 1차 풀이 : 정확성 11,14번 실패, 효율성 성공
# 2차 풀이 : 정확성 성공, 효율성 4번 실패
# 3차 풀이 성공
# # 2차 풀이에서 prefix_dict의 value를 list > dictionary로 변경
# # 변경 이유 : list보다 dictionary의 key를 통해서 찾는 것이 빠름
def solution(phone_book):
    answer = True
    prefix_dict = {}

    for p in phone_book:
        prefix_dict[p] = 1

    for number in phone_book:
        temp = ''
        for s in number:
            temp += s
            if temp in prefix_dict and temp != number:
                return False

    return answer


print(solution(["119", "97674223", "1195524421"]))  # False
print(solution(["123", "456", "789"]))  # True
print(solution(["12", "123", "1235", "567", "88"]))  # False
