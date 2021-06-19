from collections import Counter


def solution(participant, completion):
    result_dict = dict(Counter(participant) - Counter(completion))

    return list(result_dict)[0]


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"])) # "leo"
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])) # "vinko"
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])) # "mislav"
