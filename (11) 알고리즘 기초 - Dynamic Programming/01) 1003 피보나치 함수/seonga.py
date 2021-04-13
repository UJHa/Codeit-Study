# Memorization방식으로 0, 1이 호출되는 횟수를 저장함.
zero = [1, 0]
one = [0, 1]

for i in range(2, 41):  # 40까지 
    zero.append(zero[i-1]+zero[i-2])
    one.append(one[i-1]+zero[i-2])
    
# index로 접근해서 출력
for _ in range(int(input())):
    n = int(input())
    print(zero[n], zero[n])
