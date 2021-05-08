def solution(s):
    answer = []

    split_lists = s.lstrip('{').rstrip('}').split('},{')
    split_lists.sort(key=len)

    for l in split_lists:
        str_list = l.split(',')
        if len(answer) == 0:
            answer.append(int(str_list[0]))
            continue
        for i in str_list:
            if int(i) not in answer:
                answer.append(int(i))

    return answer