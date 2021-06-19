# 단어 변환
# 정확성: 100.0
# 합계: 100.0 / 100.0
from collections import deque


def can_move_word(word1, word2):
    diff = 0
    for a, b in zip(word1, word2):
        if a != b:
            diff += 1
    if diff == 1:
        return True
    return False


def solution(begin, target, words):
    if target not in words:
        return 0

    visit_check_dict = {}
    for w in words:
        visit_check_dict[w] = False

    answer = 0
    find_queue = deque()
    find_queue.append((0, begin))
    while len(find_queue) > 0:
        cur_move_count, cur_word = find_queue.popleft()
        visit_check_dict[cur_word] = True
        if cur_word == target:
            answer = cur_move_count
            break
        for word, is_visited in visit_check_dict.items():
            # 1개의 글자가 차이날 때
            if can_move_word(cur_word, word) and is_visited is False:
                find_queue.append((cur_move_count + 1, word))

    return answer


# s = solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
s = solution("hit", "cog", 	["hot", "dot", "dog", "lot", "log"])
print(s)