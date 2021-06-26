import numpy as np

def distance(keypad, left, right, number, hand):
    
    left_x, left_y = int(np.where(keypad == str(left))[0]), int(np.where(keypad == str(left))[1])
    right_x, right_y = int(np.where(keypad == str(right))[0]), int(np.where(keypad == str(right))[1])
    next_x, next_y = int(np.where(keypad == str(number))[0]), int(np.where(keypad == str(number))[1])

    right_distance = abs(right_x - next_x) + abs(right_y - next_y) 
    left_distance = abs(left_x - next_x) + abs(left_y - next_y)
    
    if right_distance > left_distance:
        return 'L'
    
    elif right_distance < left_distance:        
        return 'R'
    
    else:       
        if hand == "right":
            return 'R'
        else:
            return 'L'
    


def solution(numbers, hand):
    
    HAND = hand
    
    keypad = np.array(list(range(1,10)) + ['*', 0, '#']).reshape(4, 3)

    left_number, right_number = set([1,4,7]), set([3,6,9])
    
    left_where = '*'
    right_where = '#'
    
    answer = ''
    
    for number in numbers:
        if number in left_number:
            answer += 'L'        
            left_where = number
            
        elif number in right_number:
            answer += 'R'
            right_where = number
            
        else:
            
            answer += distance(keypad, left_where, right_where, number, HAND)
            if answer[-1] == 'L':
                left_where = number
            else:
                right_where = number
                
    return answer
    
solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
