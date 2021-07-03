def solution(array, commands):
    answer = []
    
    for commands_value in commands:
        arr_sort = sorted(array[commands_value[0]-1:commands_value[1]])
        answer.append(arr_sort[commands_value[2]-1])
        
    return answer
