# (3085) 사탕 게임
# 푸는 중...(아직 오답)
SWAP_COUNT = 1
def get_both_side_lines(line_index):
    result = []
    if line_index == 0:
        result = [line_index + 1]
    elif line_index == len(candies) - 1:
        result = [line_index - 1]
    else:
        result = [line_index - 1, line_index + 1]
    return result


def find_candy_max(candies, color):
    max_candy = 0
    # 가로 축 최대 개수 찾기
    for y in range(len(candies)):
        candy_count = 0
        swap_time = 0
        check_line = get_both_side_lines(y)

        for x in range(len(candies[0])):
            if candies[y][x] == color:
                candy_count += 1
            elif swap_time == 0:
                for line_i in check_line:
                    if candies[line_i][x] == color:
                        candy_count += 1
                        swap_time += 1
                        break
            else:
                candy_count = 0
        max_candy = max(max_candy, candy_count)

    for x in range(len(candies)):
        candy_count = 0
        swap_time = 0
        check_line = get_both_side_lines(x)

        for y in range(len(candies[0])):
            if candies[y][x] == color:
                candy_count += 1
            elif swap_time == 0:
                for line_i in check_line:
                    if candies[line_i][x] == color:
                        candy_count += 1
                        swap_time += 1
                        break
            else:
                candy_count = 0
        max_candy = max(max_candy, candy_count)


    return max_candy


n = int(input())

candies = []
for i in range(n):
    candies.append(list(input()))

# 빨간 색 최대 가능 개수 찾기
red_count = find_candy_max(candies, 'C')
blue_count = find_candy_max(candies, 'P')
green_count = find_candy_max(candies, 'Z')
yellow_count = find_candy_max(candies, 'Y')

print(red_count)
print(blue_count)
print(green_count)
print(yellow_count)

max_value = max(red_count, blue_count, green_count, yellow_count)

print(max_value)