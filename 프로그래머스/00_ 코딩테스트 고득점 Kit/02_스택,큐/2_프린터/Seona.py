# 실패
# 정확도 20%
'''
# 접근 방법
1. 인쇄 요청 문서의 중요도를 처음부터 확인하면서 중요도가 더 높은 문서가 있으면 가장 마지막으로 배치되도록 반복

'''
def solution(priorities, location):

    final_lst = list(range(len(priorities)))
    
    i = 0
    count = len(priorities)
    
    while i <= count :
        
        max_value = max(priorities)
        
        if priorities[0] != max_value:        
            final_lst.insert(count, final_lst[0])  # 마지막에 추가 
            final_lst.pop(0)  # 추가하면서 첫번째 삭제 
            priorities.pop(0)  # 비교한 priorities 삭제 
            
        i+=1
            
    return final_lst.index(location)+1
