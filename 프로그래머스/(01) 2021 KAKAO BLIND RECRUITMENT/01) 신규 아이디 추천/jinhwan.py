def get_remove_impossible_char(id):
    # 2단계 알파벳 소문자, 숫자, -, _, .만 포함한 문자열 반환
    result = ''
    for s in id:
        if s.isalpha() \
                or s.isdigit() \
                or s == '-' \
                or s == '_' \
                or s == '.':
            result += s
    return result


def get_trim_dot(id):
    # 3단계 마침표 중복 제거
    prev_str = ''
    result = ''
    for p_s in id:
        if p_s != '.':
            result += p_s
        else:  # if p_s == '.':
            if prev_str != p_s:
                result += p_s
        prev_str = p_s
    # 4단계 마침표 맨 앞, 맨뒤 제거
    if result[0] == '.':
        result = result[1:]
    if len(result) > 1 and result[-1] == '.':
        result = result[:-1]
    return result


def solution(new_id):
    answer = ''
    # 1단계
    answer = new_id.lower()

    # 2단계
    answer = get_remove_impossible_char(answer)

    # 3단계, 4단계
    answer = get_trim_dot(answer)

    # 5단계
    if len(answer) == 0:
        answer = 'a'

    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        while answer[-1] == '.':
            answer = answer[:-1]

    # 7단계
    while len(answer) <= 2:
        answer += answer[-1]
    return answer