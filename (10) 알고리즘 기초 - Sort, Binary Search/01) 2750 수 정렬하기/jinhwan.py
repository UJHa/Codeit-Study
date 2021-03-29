# (2750) 수 정렬하기
n = int(input())

num_list = []
for i in range(n):
    num_list.append(int(input()))
num_list.sort()

for j in num_list:
    print(j)