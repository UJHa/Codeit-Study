T = int(input())  # 테스트 케이스 개수

for i in range(T):
    N = int(input())
    N_lst = list(map(int, input().split()))
    
    N_lst.sort()
    
    diff_lst = []

    for i in range(len(N_lst)-1):
        diff_ = N_lst[i+1] - N_lst[i]
        diff_lst.append(diff_)
    
    print(sum(diff_lst)*2)
