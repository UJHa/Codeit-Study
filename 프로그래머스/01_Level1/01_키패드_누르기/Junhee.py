# 정확성 100 합 100 성공
# 키패드를 2D배열로 구현해 양 손가락 변수를 통해 위치를 바꿔가며 구한다. 
# 손의 위치와 숫자 위치 간의 맨하탄 거리를 구해 누를 손가락을 결정한다. 
# 숫자를 누른 뒤엔 손가락 위치 변수를 바꿔준다. 

def solution(numbers, hand):
    answer = ""
    key_pad = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9],
               ['*', 0, '#']]
    L, R = (3, 0), (3, 2)  # 초기 손가락 위치 
    
    for num in numbers:
        h, idx = determine_hand(num, key_pad, L, R, hand)
        
        if h == 'L':
            L = idx
        elif h == 'R':
            R = idx
        answer += h

    return answer


def determine_hand(num, key_pad, L, R, hand):
    for i in range(4):
        for j in range(3):
            if key_pad[i][j] == num:
                a, b = i, j  # 눌러야 할 숫자의 인덱스 (a, b)
            
    if num in (1, 4, 7):
        return 'L', (a, b)
    elif num in (3, 6, 9):
        return 'R', (a, b)
    else:
        # 맨하탄 거리 비교해 가까운 손가락 출력 
        left = abs(L[0] - a) + abs(L[1] - b)
        right = abs(R[0] - a) + abs(R[1] - b)
    
        if left < right: 
            return 'L', (a, b)
        elif left > right: 
            return 'R', (a, b)
        else:
            if hand == "left":
                return 'L', (a, b)
            elif hand == "right":
                return 'R', (a, b)
