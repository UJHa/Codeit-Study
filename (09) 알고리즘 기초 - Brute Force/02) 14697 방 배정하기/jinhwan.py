# (14697) 방 배정하기
# 푸는 중...(아직 오답)
def room_check(room_types, head_count):
    # 한 종류 방으로 배치 가능할때
    if head_count % room_types[0] == 0 or\
       head_count % room_types[1] == 0 or\
       head_count % room_types[2] == 0:
        return 1

    for room1_count in range(1, head_count // room_types[0] + 1):
        remains = head_count - room1_count * room_types[0]
        # 두 종류 방으로 배치 가능할때
        if remains % room_types[1] == 0:
            return 1
        for room2_count in range(1, head_count // room_types[1] + 1):
            remains = head_count - (room1_count * room_types[0] + room2_count * room_types[1])
            # 세 종류 방으로 배치 가능할때
            if remains % room_types[2] == 0:
                return 1
    return 0


input_datas = list(map(int, input().split()))

rooms = input_datas[0:3]
total = input_datas[3]

print(room_check(rooms, total))
