import sys

def fibonacci(n):
    
    dict = {1:0, 0:0}    

    count = 0
    
    current = 1
    previous = 0

        
    for _ in range(0, n-1):
        
        count+=1
        
        current, previous = current+previous, current
        
    dict[1] = count        
        
    
    if n>=2 or n==0:
        
        dict[0] = 1
        
    elif n == 1:
        dict[1] = 1
        
    return dict

N = int(input())
lst = []

for i in range(N):
    
    lst.append(int(input()))
 
for j in lst:
    
    ans = fibonacci(j)
    
    print(ans[0], ans[1])
