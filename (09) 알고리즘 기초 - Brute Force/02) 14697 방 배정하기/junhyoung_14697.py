# 방 배정하기
# 1, 2, 3종류를 각각 따로 구현하자!
def assign_room(room_list, student):
    # 1종류의 방만 사용
    if student % room_list[0] == 0 or student % room_list[1] == 0 or student % room_list[2] == 0:
        return 1

    # 2종류
    for index in range(len(room_list) - 1):
        i = 1
        while student - i * room_list[index] > 0:
            for other in room_list[index+1:]:
                if (student - i * room_list[index]) % other == 0:
                    return 1
            i += 1

    # 3종류
    for i in range(1, student // room_list[0]):
        for j in range(1, (student-i*room_list[0]) // room_list[1]):
            if (student - i*room_list[0] - j*room_list[1]) % room_list[2] == 0:
                return 1

    return 0


my_room = list(map(int, input().split()))
print(assign_room(my_room[:-1], my_room[-1]))
#
# print(assign_room([5, 9, 12], 113))
# print(assign_room([3, 6, 9], 112))