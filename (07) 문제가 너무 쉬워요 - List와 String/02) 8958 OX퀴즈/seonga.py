n = int(input())

for i in range(n):
    
    test = str(input())
    
    score = 0
    count = 0
    
    for j in list(test):
        if j == "O":
            count += 1
            score += count
        elif j == "X":
            count = 0
    print(score)
