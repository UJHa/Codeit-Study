def solution(number, k):
    '''k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자

    Args:
        number: 1~1,000,000 크기의 숫자인 문자열
        k: 1~(len(number)-1) 크기의 정수

    Returns:
        Answer: 만들 수 있는 가장 큰 숫자인 문자열
    '''
    num_list = [int(i) for i in number]

    answer = ""
    for i in range(len(number)-k):
        answer += str(num_list[i])

    return answer

