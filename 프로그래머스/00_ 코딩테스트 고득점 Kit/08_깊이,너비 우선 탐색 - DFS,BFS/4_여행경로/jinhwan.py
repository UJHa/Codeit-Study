# 여행경로
# 정확성: 100.0
# 합계: 100.0 / 100.0
def solution(tickets):
    answer = []
    visit_dict = {}
    for cur, next in tickets:
        visit_dict[cur] = visit_dict.get(cur, []) + [next]

    for k, v in visit_dict.items():
        visit_dict[k].sort(reverse=True)

    move_queue = []
    move_queue.append('ICN')
    while len(move_queue) > 0:
        cur_pos = move_queue[-1]
        if cur_pos not in visit_dict or len(visit_dict[cur_pos]) == 0:
            answer.append(move_queue.pop())
        else:
            move_queue.append(visit_dict[cur_pos].pop())

    return answer[::-1]


# s = solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])  # ["ICN", "JFK", "HND", "IAD"]
# s = solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]) == ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
# s = solution([["ICN", "SFO"], ["SFO", "ICN"], ["ICN", "SFO"], ["SFO", "QRE"]]) == ["ICN", "SFO", "ICN", "SFO", "QRE"]
s = solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]
) == ["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"]
print(s)