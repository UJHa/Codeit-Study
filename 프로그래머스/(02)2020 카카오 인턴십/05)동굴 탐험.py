# 1차 풀이(정확성, 효율성 성공) + 다른 직관적인 풀이를 찾아보자.

def solution(n, path, order):
    # 0: 현 위치의 이전 위치 정보 int(상위)
    # 1: 현 위치의 다음 위치 정보 list(하위)
    # 2: 필요한 이전 방문 방이 있는지 여부 int(초기값 0)
    rooms = [[] for _ in range(n)]
    for a,b in path:
        rooms[a].append(b)
        rooms[b].append(a)

    order_dict = {}
    re_order_dict = {}
    for a,b in order:
        order_dict[a] = b
        re_order_dict[b] = a

    # 방문 여부에 대한 bool table 필요
    can_visit_table = [False for _ in range(n)]
    visit_table = [False for _ in range(n)]
    queue = [0]
    visit_table[0] = True
    while queue:
        index = queue.pop(0)
        can_visit_table[index] = True
        # 방문 조건 없는 경우
        if re_order_dict.get(index) is None:
            visit_table[index] = True
            for room in rooms[index]:
                if not visit_table[room]:
                    queue.append(room)
            # 방문 조건인 방일 때 queue에 추가
            if order_dict.get(index) is not None and can_visit_table[order_dict[index]]:
                queue.append(order_dict[index])
        # 방문 조건 있는 경우
        else:
            if visit_table[re_order_dict[index]]:
                visit_table[index] = True
                for room in rooms[index]:
                    if not visit_table[room]:
                        queue.append(room)

    for i in range(n):
        if not visit_table[i]:
            return False

    return True


print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]))
print(solution(9, [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]], [[4,1],[5,2]]))
print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]]))