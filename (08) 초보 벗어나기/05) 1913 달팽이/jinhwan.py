# (1913)달팽이
# 빈 리스트 생성
def empty_list(number):
    temp_list = []
    for index in range(number):
        temp_list.append([])
        for j in range(number):
            temp_list[index].append(-1)
    return temp_list


# 달팽이 2차원 배열 값 입력
def make_snail_list(number):
    snail_box = empty_list(number)

    x, y = 0, 0
    edit_number = number * number
    direct_index = 0

    while True:
        # print(f'x : {x}\ty : {y}\t direct_index : {direct_index}\t edit_number : {edit_number}')
        snail_box[y][x] = edit_number
        if edit_number == 1:
            break

        x, y = x + direct_list[direct_index][0], y + direct_list[direct_index][1]

        if 0 <= x < number and 0 <= y < number and snail_box[y][x] == -1:
            edit_number -= 1

        if (0 <= x < number and 0 <= y < number and snail_box[y][x] != -1) \
                or not (0 <= x < number and 0 <= y < number):
            x, y = x - direct_list[direct_index][0], y - direct_list[direct_index][1]
            direct_index = (direct_index + 1) % len(direct_list)
    return snail_box


# 이동 방향의 순서 저장
direct_list = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# 정사각형 변의 크기와 찾아야 하는 자연수 입력 받기
digit = int(input())
find_number = int(input())

snail_list = make_snail_list(digit)

x, y = 0, 0
for i in range(len(snail_list)):
    line = ''
    for j in range(len(snail_list[i])):
        if find_number == snail_list[i][j]:
            x, y = i, j
        line += str(snail_list[i][j]) + ' '
    print(line)

print(x + 1, y + 1)