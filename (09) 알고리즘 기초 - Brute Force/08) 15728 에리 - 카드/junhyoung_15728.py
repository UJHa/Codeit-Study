# 에리 - 카드

# 점수 리스트(사용한 공유카드, 팀 카드, 점수가 기록)를 만들어 내림차순 정렬한다.
# 점수 리스트는 가장 높은 점수가 처음으로 오게 정렬된다.
# 견제된 팀카드가 포함된 리스트는 제외한 나머지 리스트중에서 처음 리스트가 가장 크다.
# 이 때의 리스트를 출력한다.
def max_score(total, limit, share, team):
    score = []
    # [공유카드중 한장, 팀카드중 한장, 점수]
    # [[-1, -1, 1], [-1, 0, 0],,] 이런식으로 리스트를 만든다.
    for s in share:
        for t in team:
            score.append([s, t, s*t])

    # 내림차순 정렬
    score = sorted(score, key=lambda x: x[2], reverse=True)

    limit_card = [score[0][1]]
    i = 1
    while len(limit_card) <= limit:
        if score[i][1] not in limit_card:
            limit_card.append(score[i][1])
            # k장 팀 견제 카드에 추가한 후,
            # 남아있는 팀 카드와 공유 카드의 곱(점수)이 가장 큰 경우의 인덱스 i를 가지고 반복문 탈출
            if len(limit_card) == limit+1:
                break
        i += 1

    return score[i][2]


total_card, limit_num = map(int, input().split())
share_card = list(map(int, input().split()))
team_card = list(map(int, input().split()))

print(max_score(total_card, limit_num, share_card, team_card))
# print(max_score(5, 2, [-1, 2, 3, 4, 5], [-1, 0, 2, 3, 4]))
# print(max_score(2, 2, [-1, 4], [3, 5]))