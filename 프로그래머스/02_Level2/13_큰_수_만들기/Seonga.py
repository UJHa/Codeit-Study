# 시간 초과로 실패 
from itertools import combinations

def solution(number, k):

    number = list(number)

    com_lst = list(combinations(number, len(number)-k))

    com_value_lst = []

    for tuple_ in com_lst:

        final_tuple_value = ''

        for tuple_value in tuple_:
             final_tuple_value += tuple_value 

        com_value_lst.append(int(final_tuple_value))

    answer = max(com_value_lst)
    
    return str(answer)
