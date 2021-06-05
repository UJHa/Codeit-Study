# 실패 
# 정확도 86.7

'''
# 접근 방안
1. 재생된 장르에 대한 재생 횟수 합 딕셔너리(dict_genre_sum), 재생 횟수 index 딕셔너리를 통해 접근(dict_genre_index)
2. dict_genre_sum에서 최댓값을 가지는 장르를 찾아 dict_genre_index에서 재생 횟수 index 추출

# 해결해야 할 문제
1. 장르 내 재생 횟수가 같은 노래는 인덱스 고유 번호가 낮은 노래를 먼저 수록하도록 
'''

# -*- coding: utf-8 -*-


def find_index(origin_list, word):
    
    blank_lst = []
    list_ = origin_list
    while True:
        try:
            blank_lst.append(list_.index(word) + (blank_lst[-1] + 1 if len(blank_lst) != 0 else 0))
            list_ = origin_list[blank_lst[-1]+1:]
        except:
            break
        
    return blank_lst
        
def get_multi_index(origin_list, index):  # 인덱스 여러 개인 경우 
    return [origin_list[i] for i in index]

def solution(geners, plays):
    
    dict_genre_sum = {}
    dict_genre_index = {}
        
    genere_lst = list(set(geners))

    for genere_value in genere_lst:
        
    
        index_lst = find_index(geners, genere_value)
        dict_genre_index[genere_value] = index_lst
        dict_genre_sum[genere_value] =sum(get_multi_index(plays, index_lst))
        
    final_lst = []
    
    while len(dict_genre_sum.keys()) > 0:
        
        output_lst = []

        max_key = max(dict_genre_sum, key = lambda key: dict_genre_sum[key])  # 많이 재생된 장르 추출 
        max_key_plays = get_multi_index(plays, dict_genre_index[max_key])  # 많이 재생된 장르의 plays 인덱스 추출
    
        while len(max_key_plays) > 0:
        
            max_value = max(max_key_plays)
            max_index = find_index(plays, max_value)
            
            if len(max_index) == 1:
                output_lst.append(max_index[0])
                
            else:
                for index_value in max_index:
                    
                    if index_value not in sum(final_lst, []):
                        output_lst.append(index_value)
                        
            max_key_plays.remove(max_value)

            if len(output_lst)==2:
                break
            
        final_lst.append(output_lst)
        
        dict_genre_sum.pop(max_key)
            
    return sum(final_lst, [])


solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
