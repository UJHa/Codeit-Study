# 단어 변환
# 정확성: 60.0
# 합계: 60.0 / 100.0
from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0

    visit_check_dict = {}
    for w in words:
        visit_check_dict[w] = False

    answer = 0
    find_queue = deque()
    find_queue.append(begin)
    while len(find_queue) > 0:
        cur_word = find_queue.pop()
        visit_check_dict[cur_word] = True
        answer += 1
        if cur_word == target:
            break
        for word, is_visited in visit_check_dict.items():
            # 1개의 글자가 차이날 때
            if len(set(cur_word + word)) == len(cur_word) + 1 and is_visited is False:
                if word not in find_queue:
                    find_queue.append(word)

    return answer - 1


# s = solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
s = solution("hit", "cog", 	["hot", "dot", "dog", "lot", "log"])
print(s)
