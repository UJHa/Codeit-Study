# 다리를 지나는 트럭(성공)
# 정확성: 100.0
# 합계: 100.0 / 100.0
def move_trucks(cross_list):
    for c in cross_list:
        c[1] += 1


def is_finish_truck(truck_distance, bridge_length):
    return truck_distance == bridge_length


def solution(bridge_length, weight, truck_weights):
    answer = 0

    wait_list = truck_weights  # 다리를 지나가지 않은 리스트
    crossing_list = []  # 다리에 올라간 리스트
    finish_list = []  # 다리를 지나간 리스트

    # 다리의 현재 가중 무게
    bridge_weight = 0

    truck_count = len(truck_weights)
    while len(finish_list) < truck_count:
        print(wait_list, crossing_list, finish_list)
        answer += 1
        if len(crossing_list) != 0:
            # 다리 위의 트럭들 1칸씩 이동
            move_trucks(crossing_list)
            # 이동한 트럭들 중에서 다리를 건넜으면 crossing_list에서 제거
            if is_finish_truck(crossing_list[0][1], bridge_length):
                crossing_truck_data = crossing_list.pop(0)
                c_truck_weight = crossing_truck_data[0]
                bridge_weight -= c_truck_weight
                finish_list.append(c_truck_weight)

        # 매 초마다 대기 트럭 있으면 bridge에 추가
        if len(wait_list) != 0:
            w_truck_weight = wait_list[0]
            if bridge_weight + w_truck_weight <= weight:
                wait_list.pop(0)
                crossing_list.append([w_truck_weight, 0])
                bridge_weight += w_truck_weight

    print(wait_list, crossing_list, finish_list)

    return answer


s = solution(2, 10, [7, 4, 5, 6])  # 8
print(s)
