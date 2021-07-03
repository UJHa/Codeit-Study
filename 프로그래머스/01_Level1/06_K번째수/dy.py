def solution(array, commands):
    answer = []
    pieces = []
    
    for i in range(len(commands)):
        pieces = array[commands[i][0] - 1 : commands[i][1]]
        pieces.sort()
        answer.append(pieces[commands[i][2] - 1])
        
    return answer
