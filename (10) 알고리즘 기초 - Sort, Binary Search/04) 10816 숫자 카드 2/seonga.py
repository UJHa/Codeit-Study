## 수찾기 코드처럼 작성하면 시간초과 뜸.

# LST1, LST2 모두 정렬 후 처음부터 차례대로 개수 파악
# LST1의 인덱스 값이 찾고자하는 값보다 크면 인덱스만 +1
N = int(input())
LST1= list(map(int, input().split()))

M = int(input())
LST2= list(map(int, input().split()))

index, dic = 0, {}
LST1.sort()

for value in sorted(LST2):  # 찾고자하는 값 
    count = 0    # 개수 세릴 변수 
    if value not in dic:  # dic에 찾고자하는 값이 없다면 
        while index < len(LST1):  # LST1의 길이만큼 반복 
            if value == LST1[index]:  # LST1의 첫번째 인덱스부터 확인하여 값이 있으면 +1
                count +=1
                index +=1
            elif value > LST1[index]:
                index += 1
            else:
                break
        dic[value] = count 

for elem in LST2:
    print(dic[elem], end = ' ') 

    
