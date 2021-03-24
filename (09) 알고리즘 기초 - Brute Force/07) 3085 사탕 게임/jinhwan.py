# (3085) 사탕 게임
def shuffle(check_candies, pos_x, pos_y, direction):
    change_target_x = x + direction[0]
    change_target_y = y + direction[1]

    # 바꾸려는 사탕 위치가 배열 밖일 때 무시하도록 조건 설정
    if change_target_x < 0 or change_target_x > n - 1 \
            or change_target_y < 0 or change_target_y > n - 1:
        return

    candies[y][x], candies[change_target_y][change_target_x] = candies[change_target_y][change_target_x], candies[y][x]


def get_eat_count(candies, pos_x, pos_y):
    check_color = candies[pos_y][pos_x]
    # print(check_color)

    # 가로 축 최대 길이 파악
    index = pos_x
    x_length = 0
    while index < len(candies[pos_y]):
        if candies[pos_y][index] == check_color:
            x_length += 1
        else:
            break
        index += 1

    index = pos_x
    while index >= 0:
        if candies[pos_y][index] == check_color:
            x_length += 1
        else:
            break
        index -= 1

    x_length -= 1

    # 세로 축 최대 길이 파악
    index = pos_y
    y_length = 0
    while index < len(candies):
        if candies[index][pos_x] == check_color:
            y_length += 1
        else:
            break
        index += 1

    index = pos_y
    while index >= 0:
        if candies[index][pos_x] == check_color:
            y_length += 1
        else:
            break
        index -= 1

    y_length -= 1
    return max(x_length, y_length)


n = int(input())

candies = []
for i in range(n):
    candies.append(list(input()))

directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

max_eat_count = 0
for y in range(n):
    for x in range(n):
        for d in directions:
            # print(f'test {x} {y}')
            # 인접 칸과 교환하기
            shuffle(candies, x, y, d)

            max_eat_count = max(max_eat_count, get_eat_count(candies, x, y))

            # 원래대로 돌려 놓기
            shuffle(candies, x, y, d)

print(max_eat_count)
