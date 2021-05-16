def solution(new_id):
    return s7(s6(s5(s4(s3(s2(s1(new_id)))))))


# 모든 대문자를 소문자로 치환
def s1(tmp_id):
    tmp_id = tmp_id.lower()
    return tmp_id


# 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
def s2(tmp_id):
    rslt = ""
    for i in tmp_id:
        if i.isalpha() or i.isdigit() or i in ['-', '_', '.']:
            rslt += i
    return rslt
    
    
# 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
def s3(tmp_id):
    while ".." in tmp_id:
        tmp_id = tmp_id.replace("..", '.')
    return tmp_id


# 마침표(.)가 처음이나 끝에 위치한다면 제거
def s4(tmp_id):
    if tmp_id[0] == '.':
        tmp_id = tmp_id[1:]
    if len(tmp_id) >= 1 and tmp_id[-1] == '.':
        tmp_id = tmp_id[:-1]
    return tmp_id


# 빈 문자열이라면 'a'를 대입
def s5(tmp_id):
    if not tmp_id:
        tmp_id = 'a'
    return tmp_id


# 16자 이상이면 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
# 만약 제거 후 마침표(.)가 끝에 위치한다면 제거
def s6(tmp_id):
    if len(tmp_id) >= 16:
        tmp_id = tmp_id[:15]
        if tmp_id[-1] == '.':
            tmp_id = tmp_id[:-1]
    return tmp_id


# 2자 이하라면 마지막 문자를 길이가 3이 될 때까지 반복해서 끝에 붙임 
def s7(tmp_id):
    if len(tmp_id) <= 2:
        tmp_id += tmp_id[-1] * (3-len(tmp_id))
    return tmp_id