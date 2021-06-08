# 더 맵게(성공)
# 정확성: 76.2
# 효율성: 23.8
# 합계: 100.0 / 100.0
import heapq


def solution(scoville, K):
    answer = 0
    # 힙 자료구조로 스코빌 리스트 넣어서 정렬
    heapq.heapify(scoville)

    while len(scoville) > 1 and scoville[0] < K:
        # 정렬된 힙에서 0번 인덱스는 최소값이 보장됨
        mix_scoville = heapq.heappop(scoville)
        mix_scoville = mix_scoville + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, mix_scoville)
        answer += 1

    if len(scoville) == 1 and scoville[0] < K:
        answer = -1
    return answer


s = solution([1, 2, 3, 9, 10, 12], 7)  # 1
print(s)
