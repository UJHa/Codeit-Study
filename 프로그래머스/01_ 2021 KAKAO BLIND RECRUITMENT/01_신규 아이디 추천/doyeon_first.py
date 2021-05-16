def solution(new_id):
    # 1 step
    new_id = new_id.lower()

    # 2 step
    answer = ''
    for ch in new_id:
        if ch.isalpha() or ch.isdigit() or ch in '-_.':
            answer += ch

    # 3 step
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4 step
    f = answer[0]
    l = answer[-1]
    if f == '.':
        answer = answer[1:]
    if l == '.':
        answer = answer[:-1]

    # 5 step
    if answer == '':
        answer = 'a'

    # 6 step
    if len(answer) >15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7 step
    while len(answer) < 3:
        answer += answer[-1]

    return answer
