# 뉴스 클러스터링
# 정확성: 100.0
# 합계: 100.0 / 100.0

def get_lower_set_dict(_str):
    result = {}
    for i in range(len(_str) - 1):
        if _str[i].isalpha() and _str[i+1].isalpha():
            key = _str[i:i + 2].lower()
            if result.get(key) is None:
                result[key] = 0
            result[key] += 1

    return result


def solution(str1, str2):
    set_str1, set_str2 = get_lower_set_dict(str1), get_lower_set_dict(str2)
    # print(set_str1, set_str2, len(set_str1), len(set_str2))
    keys = list(set_str1.keys()) + list(set_str2.keys())

    intersection_count, union_count = 0, 0
    # 교집합 구하기
    for k in set(keys):
        intersection_count += min(set_str1.get(k, 0), set_str2.get(k, 0))

    # 합집합 구하기
    for k in set(keys):
        union_count += max(set_str1.get(k, 0), set_str2.get(k, 0))
    # print(intersection_count, union_count)

    if intersection_count == 0 and union_count == 0:
        answer = 1
    else:
        answer = intersection_count / union_count

    return (answer * 65536) // 1


s = solution('FRANCE', 'french') == 16384
# s = solution('handshake', 'shake hands') == 65536
# s = solution('aa1+aa2', 'AAAA12') == 43690
# s = solution('E=M*C^2', 'e=m*c^2') == 65536
print(s)
