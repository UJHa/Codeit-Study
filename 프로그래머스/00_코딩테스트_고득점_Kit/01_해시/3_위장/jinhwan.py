def solution(clothes):
    answer = 1
    cloth_dict = {}
    for c in clothes:
        cloth_type = c[1]
        if cloth_type not in cloth_dict:
            cloth_dict[cloth_type] = 1
        else:
            cloth_dict[cloth_type] += 1

    for k in cloth_dict.keys():
        answer *= (cloth_dict[k] + 1)

    answer -= 1
    return answer


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))  # 5
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))  # 3