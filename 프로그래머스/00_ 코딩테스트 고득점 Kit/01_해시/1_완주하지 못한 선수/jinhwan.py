def solution(participant, completion):
    answer = ''
    completion_dict = {}
    for c in completion:
        if completion_dict.get(c) is None:
            completion_dict[c] = 1
        else:
            completion_dict[c] += 1

    for p in participant:
        if completion_dict.get(p) is None:
            completion_dict[p] = 0

        if completion_dict[p] == 0:
            answer = p
            break
        else:
            completion_dict[p] -= 1

    return answer

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"])) # "leo"
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])) # "vinko"
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])) # "mislav"
