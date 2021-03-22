# https://www.acmicpc.net/problem/14697

def room():
  
    # 입력 받음 
    A_ROOM, B_ROOM, C_ROOM, STUDENT = list(map(int, input().split()))
        
    # 1~학생수 범위까지 방에 들어갈 수 있는 사람수를 띄어넘어가며 경우의 수 계산 
    for a_student in range(0, STUDENT + 1, A_ROOM):  
        for b_student in range(0, STUDENT + 1, B_ROOM):
            for c_student in range(0, STUDENT + 1, C_ROOM):
                
                # 빈 침대 없이 배정가능한 경우 
                if a_student + b_student + c_student == STUDENT:
                    
                    return 1  
    # 빈 침대 없이 배정할 수 없는 경우                 
    return 0
            
print(room())  # 76ms
