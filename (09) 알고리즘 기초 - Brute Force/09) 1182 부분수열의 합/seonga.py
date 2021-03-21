from itertools import combinations

def partitional_sequence(n, sum_m, lst):
    
    count = 0
    
    for i in range(1, len(lst)+1):
        lst_com = list(combinations(lst,i))
        for list_value in lst_com:
            if sum(list_value) == sum_m:
                count += 1
                
    return count

n, sum_m = map(int, input().split())
lst = list(map(int, input().split()))
    
print(partitional_sequence(n, sum_m, lst))
