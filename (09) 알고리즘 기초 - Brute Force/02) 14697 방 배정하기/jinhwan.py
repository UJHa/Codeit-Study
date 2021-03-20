# (14697) 방 배정하기
def room_check(room_types, head_count):
    # 한 종류 방으로 배치 가능할때
    for room1_members in range(0, head_count + 1, room_types[0]):
        for room2_members in range(0, head_count + 1, room_types[1]):
            for room3_members in range(0, head_count + 1, room_types[2]):
                if total == room1_members + room2_members + room3_members:
                    return 1
    return 0


input_datas = list(map(int, input().split()))

rooms = input_datas[0:3]
total = input_datas[3]

print(room_check(rooms, total))
