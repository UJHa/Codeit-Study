# 음양 더하기
def solution(absolutes, signs):
    answer = 0
    for a, s in zip(absolutes, signs):
        add_num = a
        if s is False:
            add_num = -add_num
        answer += add_num
    return answer


s = solution([4,7,12], [True,False,True])
# s = solution([1,2,3], [False,False,True])
print(s)