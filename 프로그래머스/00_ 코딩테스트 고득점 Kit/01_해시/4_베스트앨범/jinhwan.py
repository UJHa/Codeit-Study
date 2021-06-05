def play_dicts_count(data):
    return data[1][1]


def play_count(data):
    return data[1]


def solution(genres, plays):
    answer = []
    # 고유번호의 데이터 dictionary 생성
    play_dict = {}
    for i in range(len(genres)):
        play_dict[i] = [genres[i], plays[i]]

    # 내림차순으로 플레이 리스트 정렬
    play_upper_list = sorted(play_dict.items(), key=play_dicts_count, reverse=True)

    # 속한 노래 많이 재생된 순서 파악
    genre_upper_dict = {}
    for key, val in play_dict.items():
        genre_upper_dict[val[0]] = genre_upper_dict.get(val[0], 0) + val[1]

    genre_upper_list = sorted(genre_upper_dict.items(), key=play_count, reverse=True)

    # answer 저장 시작
    MAX_COUNT = 2
    for el in genre_upper_list:
        genre = el[0]
        count = 0
        for val in play_upper_list:
            if count == MAX_COUNT:
                break

            if val[1][0] == genre:
                answer.append(val[0])
                count += 1

    print(answer)

    return answer