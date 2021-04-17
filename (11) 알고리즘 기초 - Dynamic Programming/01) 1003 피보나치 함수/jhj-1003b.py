'''
1. 값 저장할 리스트 count0, count1 만들기
2. n = 2~41 까지 전처리(count0, count1 채우기) 하기
3. 값 불러오기
'''

count0 = [1, 0]
count1 = [0, 1]

for i in range(2, 41):
    count0.append(count0[i - 1] + count0[i - 2])
    count1.append(count1[i - 1] + count1[i - 2])

for _ in range(int(input())):
    n = int(input())
    print(count0[n], count1[n])
