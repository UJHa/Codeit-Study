
def obey_rule(place):
    manhattans_1 = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    manhattans_2 = [(0, -2), (0, 2), (-2, 0), (2, 0)]
    manhattans_3 = [(-1, -1), (1, 1), (-1, 1), (1, -1)]

    for p in place:
        print(p)

    for y, p in enumerate(place):
        print(y, p)
        for x, room in enumerate(p):
            print(x, room)
            if room == 'P':
                # 상하좌우 : 맨해튼 거리 1
                for mx, my in manhattans_1:
                    dx, dy = x + mx, y + my
                    if 0 <= dx < 5 and 0 <= dy < 5:
                        if place[dy][dx] == 'P':
                            print('False : ', x, y, dx, dy, mx, my)
                            return False

                # 상하좌우 : 맨해튼 거리 2
                for mx, my in manhattans_2:
                    dx, dy = x + mx, y + my
                    if 0 <= dx < 5 and 0 <= dy < 5:
                        if place[dy][dx] == 'P':
                            if place[(dy+y)//2][(dx+x)//2] == 'X':
                                pass
                            else:
                                print('Fals2 : ', x, y)
                                return False

                # 대각선 거리 : 맨해튼 거리 2
                for mx, my in manhattans_3:
                    dx, dy = x + mx, y + my
                    if 0 <= dx < 5 and 0 <= dy < 5:
                        if place[dy][dx] == 'P':
                            if place[dy][x] == 'X' and place[y][dx] == 'X':
                                pass
                            else:
                                print('False3 : ', x, y)
                                return False
    return True

def solution(places):
    answer = []
    for place in places:
        if not obey_rule(place):
            answer.append(0)
        else:
            answer.append(1)
    return answer
