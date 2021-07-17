def solution(s):
    answer = 1001

    for i in range(1, len(s)//2+1):
        answer = min(answer, zip_count(i, s))

    if answer > len(s):
        answer = len(s)

    return answer


def zip_count(n, s):
    """문자열을 압축해 길이를 구하는 함수

    Args:
        n: 압축할 단위 숫자
        s: 압축할 문자열
        zip_str: 압축된 문자열
        tmp_str: 중복 문자열 
        zip_cnt: 중복 문자열 개수 

    Returns:
        zip_str의 총 길이 정수 
    """
    zip_str, tmp_str = "", s[:n]
    zip_cnt = 1
    
    for i in range(n, len(s), n):
        if tmp_str == s[i:i+n]:
            zip_cnt += 1
        elif zip_cnt == 1:
            zip_str += tmp_str
            tmp_str = s[i:i+n]
        else:
            zip_str += str(zip_cnt) + tmp_str
            tmp_str = s[i:i+n]
            zip_cnt = 1
    
    if zip_cnt == 1:
        zip_str += tmp_str
    else:
        zip_str += str(zip_cnt) + tmp_str

    return len(zip_str)

