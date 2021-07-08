
def solution(n, lost, reserve):
    
    n_idx = [1]*n # 인원 수만큼 배열 만들기
    
    for r in reserve:  # 체육복 여분있는 사람 인덱스
        n_idx[r-1] += 1 
    
    for l in lost:  # 체육복 잃어버린 사람 인덱스
        n_idx[l-1] -= 1
        
    for i, value in enumerate(n_idx):  # 앞 뒤 사람 확인해서 빌려주기
        if i > 0 and value == 0 and n_idx[i-1] == 2:
            n_idx[i] = 1 # 0 -> 1
            n_idx[i-1] = 1 # 2 -> 1
            
        elif i < n-1 and value == 0 and n_idx[i+1] ==2:
            n_idx[i] = 1
            n_idx[i+1] = 1
        
    return (n - n_idx.count(0))  # 전체 명수에서 옷을 안가지고 있는 사람을 빼줌
