n = int(input())
people = list(map(int, input().split()))        
seat = [0] * 101 
refused = 0 

for i in people:
    if seat[i] != 0:
        refused  += 1
    else:
        seat[i] += 1

print(refused)
