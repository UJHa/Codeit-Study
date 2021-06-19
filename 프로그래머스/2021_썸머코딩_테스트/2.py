def solution(t, r):
    answer = []
    client_list = []
    for i in range(len(t)):
        # id, 도착시간, 등급의 리스트를 client list에 추가
        client_list.append((i,t[i], r[i]))
    print(client_list)

    time_index = 0
    while len(answer) != len(t):
        can_on_list = []
        for client in client_list:
            if client is None:
                continue
            if client[1] <= time_index:
                can_on_list.append(client)
        if len(can_on_list) == 0:
            pass
        # 같은 시간 가능한 탑승자 1명
        elif len(can_on_list) == 1:
            add_index = can_on_list[0][0]
            answer.append(add_index)
            client_list[add_index] = None
        else:
            can_on_list.sort(key= lambda x: x[2])
            low_rank_list = []
            low_rank = can_on_list[0][2]
            for lrank in can_on_list:
                if low_rank == lrank[2]:
                    low_rank_list.append(lrank)
            print('low_rank_list', low_rank_list)
            if len(low_rank_list) == 1:
                add_index = low_rank_list[0][0]
                answer.append(add_index)
                client_list[add_index] = None
            else:
                low_rank_list.sort(key=lambda x:x[0])
                add_index = low_rank_list[0][0]
                answer.append(add_index)
                client_list[add_index] = None

        time_index += 1
        print(time_index, len(answer), len(t), )
        # print('can_on_list', can_on_list, client_list)

    return answer


print(solution([0,1,3,0], [0,1,2,3])) # [0, 1, 3, 2]
# print(solution([7,6,8,1], [0,1,2,3])) # 	[3, 1, 0, 2]