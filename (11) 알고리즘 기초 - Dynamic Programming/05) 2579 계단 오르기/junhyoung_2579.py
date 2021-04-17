# 2579 계단 오르기
# 아직 완료못함.
import sys


def solve(stair_num, stair_list):
    max_list = [0]
    # 계단수가 1, 2 일 경우
    if stair_num < 3:
        for i in range(1, stair_num+1):
            max_list.append(max_list[i - 1] + stair_list[i])

    # 계단수가 3개 이상
    elif stair_num >= 3:
        for i in range(1, 3):
            max_list.append(max_list[i-1] + stair_list[i])

        for i in range(3, stair_num+1):
            # i 번째 계단 까지 올라가는데 i-1 번째 계단에서 i 로 오르는 경우, i-2 번째 계단에서 i 로 오르는 경우 둘 중 큰 값(점수)를 얻는 경우 리턴
            max_list.append(max(max_list[i-3] + stair_list[i-1] + stair_list[i], max_list[i-2] + stair_list[i]))

    print(max_list[stair_num])


if __name__ == "__main__":
    my_stair_num = int(sys.stdin.readline())
    my_stair_list = [0]

    for _ in range(my_stair_num):
        my_stair_list.append(int(sys.stdin.readline()))

    solve(my_stair_num, my_stair_list)
