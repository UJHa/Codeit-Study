# 1: orders에서 각 course의 요소(size)에 해당하는 크기의 가능한 조합을 모두 combs에 담는다. (itertools.combinations())
# 2: combs에서 중복된 빈도수가 높은 조합들부터 나열하여 most_ordered에 담는다. (collections.Counter().most_common())
# 3: most_ordered에서 빈도수 2 이상인 조합들을 문자열 형태로 만들어 result에 담는다. (''.join())
# 4: result에 담긴 문자열들을 정렬하여 return한다. 
# 5: 실패! 

from itertools import combinations
from collections import Counter


def solution(orders, course):
    result = []

    for size in course:
        combs = []
        for order in orders:
            combs += combinations(sorted(order), size)

        most_ordered = Counter(combs).most_common()
        for comb in most_ordered:
            if comb[1] >= 2 and len(comb[0]) == size:
                comb_str = ''.join(comb[0])
                if comb_str not in result:
                    result.append(comb_str)
    
    return sorted(result)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))