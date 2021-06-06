# 베스트앨범(성공)
# 정확성: 100.0
# 합계: 100.0 / 100.0

def get_sort_genre_list(genres, plays):
    play_genre_dict = {}
    # 장르에 속한 곡 재생 횟수의 합을 play_genre_dict에 저장
    for g, p in zip(genres, plays):
        if play_genre_dict.get(g) is None:
            play_genre_dict[g] = 0
        play_genre_dict[g] += p

    # 장르 순서로 정렬
    play_genre_dict = sorted(play_genre_dict.items(), key=lambda x: x[1], reverse=True)
    sort_play_genre_list = [i[0] for i in play_genre_dict]
    return sort_play_genre_list


def get_sort_song_list(genres, plays, genre_list):
    # (index, genre, play)형식으로 저장하는 dict 생성
    song_dict = {}
    for i, g in enumerate(genres):
        song_dict[i] = [g, plays[i]]

    # 각 genre 별로 list 생성
    genre_list_dict = {}
    for g in genre_list:
        if genre_list_dict.get(g) is None:
            genre_list_dict[g] = []
        for key, val in song_dict.items():
            if g == val[0]:
                genre_list_dict[g].append((key, val[0], val[1]))

    # 각 리스트 정렬
    for g in genre_list:
        genre_list_dict[g].sort(key=lambda x: (-x[2], x[0]))

    return genre_list_dict


def solution(genres, plays):
    # 많이 재생된 장르 순서 리스트 만들기(1번 조건 : 재생한 장르 순서 리스트 생성)
    genre_list = get_sort_genre_list(genres, plays)

    # 각 노래의 순서 정렬(2번, 3번 내용 함수 내부에서 처리)
    get_song_data = get_sort_song_list(genres, plays, genre_list)

    # 각 장르별 2개씩 추출
    answer_list = []
    for val in get_song_data.values():
        song_list = val
        answer_list += song_list[:2]

    answer = [i[0] for i in answer_list]
    return answer


s = solution(["classic", "pop", "pop", "classic", "classic", "pop"], [500, 600, 600, 150, 800, 2500])
print(s)
