'''
n, k 인풋
공유숫자카드, 팀 숫자카드 입력
공유X팀 카드로 가능한 수 전부 구한 후 순서대로 나열
가장 큰 수에 사용된 팀 카드 삭제, 그 팀 카드를 사용한 공유X팀 카드 값 삭제
제외 과정을 count로 세 가면서 k에 도달하면 멈추기
멈춘 시점에서 공유X팀 카드 최대값 리턴



'''

def ericard():

    n, k = map(int, input().split())
    count = 0
    shared_team_card = [list(map(int, input().split())) for i in range(2)]
    multiple_card = {(shared, team):shared*team for shared in shared_team_card[0] for team in shared_team_card[1]}
    multiple_card_tuple = list(multiple_card.items())
    multiple_card_sorted = sorted(multiple_card.values(), reverse=True)

    while count < k:
        saved_tuple = []
        delete_card = 0
        for tuple in multiple_card_tuple:
            if tuple[1] == multiple_card_sorted[0]:
                delete_card = tuple[0][1]
                break
        for tuple in multiple_card_tuple:
            if tuple[0][1] == delete_card:
                saved_tuple.append(tuple)
                del multiple_card[tuple[0]]
        multiple_card_sorted = sorted(multiple_card.values(), reverse=True)
        while len(saved_tuple) > 0:
            multiple_card_tuple.pop(multiple_card_tuple.index(saved_tuple[0]))
            saved_tuple.pop(0)
        count += 1

    print(multiple_card_sorted[0])

    return 0

ericard()