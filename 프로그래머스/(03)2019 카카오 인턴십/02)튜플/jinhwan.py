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

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
