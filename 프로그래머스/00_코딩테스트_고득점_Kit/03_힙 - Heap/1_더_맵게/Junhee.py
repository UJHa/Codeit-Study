# 정확성 76.2 효율성 23.8 합 100 성공
# 최소 힙을 구현하여 푼다
import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville) >= 2:
        # 모든 음식이 최소 K 이상의 스코빌 지수인가?
        hot = heapq.heappop(scoville)
        if hot >= K:
            break
        
        # 섞기
        second_hot = heapq.heappop(scoville)
        heapq.heappush(scoville, hot+second_hot*2)
        answer += 1
    
    # 출력
    if scoville[0] >= K:
        return answer
    else:
        return -1
