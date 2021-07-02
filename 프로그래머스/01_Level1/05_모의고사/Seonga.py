
from itertools import chain, repeat

def correct_answer_count(person, answers):
    cnt = 0
    i = 0
    while i < len(answers):
        if person[i] == answers[i]:
            cnt += 1
                    
        i +=1
    return cnt
        

def solution(answers):
    
    person_1 = list(chain.from_iterable(repeat([1,2,3,4,5], int(len(answers)//len([1,2,3,4,5]))+1)))
    person_2 = list(chain.from_iterable(repeat([2, 1, 2, 3, 2, 4, 2, 5], int(len(answers)//len([2, 1, 2, 3, 2, 4, 2, 5]))+1)))
    person_3 = list(chain.from_iterable(repeat([3, 3, 1, 1, 2, 2, 4, 4, 5, 5], int(len(answers)//len([3, 3, 1, 1, 2, 2, 4, 4, 5, 5]))+1)))
    
    correct_dict = {1:correct_answer_count(person_1, answers), 2:correct_answer_count(person_2, answers), 3: correct_answer_count(person_3, answers)}
    max_value = max(correct_dict.values())
    
    winner = []
    
    for key, value in correct_dict.items():
        if value == max_value:
            winner.append(key)

    return winner
    
