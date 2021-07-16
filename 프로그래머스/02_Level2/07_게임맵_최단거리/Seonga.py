from collections import deque

d = [[1,0], [-1, 0], [0,1], [0,-1]]  # 상하좌우로 이동하기 위해 

def solution(maps):
    r = len(maps)
    c = len(maps[0])
    
    # 방문했는지 확인 할 배열
    arr = [[-1 for _ in range(c)] for _ in range(r)]  # map크기 만큼 배열 생성 
    
    q = deque() # 큐 이용
    
    q.append([0,0])  # 큐의 시작점 
    arr[0][0] = 1  # 시작 시점응ㄴ 무조건 방문 
    
    while q:  # q에 값이 없을 때까지 반복
        
        y, x = q.popleft()  # 값을 꺼내서 x, y에 할당 

        for i in range(4):  # 상하좌우 확인 
            dy = y + d[i][0]
            dx = x + d[i][1]

            if -1< dy <r and -1< dx <c: # dx, dy가 map 을 벗어나지 않을 때 동작 
                if maps[dy][dx] == 1:  # 벽으로 막혀있지 않고 
                    if arr[dy][dx] == -1:  # 방문한 적이 없는 곳 
                        arr[dy][dx] = arr[y][x] + 1  # 위치 방문 현재 위치에서 한 칸 앞으로 간 위치 
                        q.append([dy, dx])

    answer = arr[-1][-1]  # 도착지점의 최단거리 값
    
    return answer
