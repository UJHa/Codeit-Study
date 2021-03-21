from itertools import combinations  # combinations 조합 모듈 (순열 모듈도 존재)

def partitional_sequence(n, sum_m, lst):
    
    count = 0
    
    for i in range(1, len(lst)+1):
        lst_com = list(combinations(lst,i))  # lst에서 i개 만큼 뽑는 모든 경우의 수 추출 
        
        for list_value in lst_com:   # 추출된 경우의 수 반복적으로 돌면서 합 확인 
            if sum(list_value) == sum_m:
                count += 1
                
    return count

n, sum_m = map(int, input().split())
lst = list(map(int, input().split()))
    
print(partitional_sequence(n, sum_m, lst))
