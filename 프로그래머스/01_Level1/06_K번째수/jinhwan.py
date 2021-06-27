# K번째 수
def solution(array, commands):
    answer = []
    for c in commands:
        i, j, k = c
        temp = array[i-1:j]
        answer.append(sorted(temp)[k-1])
    return answer


s = solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]) == [5, 6, 3]
print(s)