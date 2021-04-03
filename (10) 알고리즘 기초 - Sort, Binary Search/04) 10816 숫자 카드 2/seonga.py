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

'''
# LST2를 정렬하는 이유 

결론부터 말씀드리면 index를 for 밖에서 초기화시키기 때문에  for문 내에서는 찾을 값 리스트도 정렬해야 함.

LST1 = [-10, -10, 2, 3, 10]
LST2 = [10, 2] 

만약 LST2를 정렬하지 않고 위와 같은 리스트를 돌린다고 가정할 때 10을 찾기 위해 index는 4로 변하고 index는 for문 밖으로 정의했기 때문에 4의 값을 가진 채로 다음 찾을 값인 2를 비교.

2는 LST1[4] = 10보다 작기 때문에 else 문으로 빠져 break되어 잘못된 결과를 출력 

하지만 정렬해준다면 2를 찾기 위해 index는 2로 변하고 다음 찾을 값인 10은 LST1[2] = 2보다 크기 때문에 elif문으로 빠져서  

index += 1, LST1[3] = 3보다 찾을 값인 value 10이 더 크기 때문에 elif문 그 다음은 if 문으로 동작해서 원하는 결과를 출력

마지막 출력할 때는 입력으로 받은 순서대로 출력해야하기 때문에 LST1처럼 sort 메소드를 사용하는 것이 아닌 sorted 함수를 사용해야 합니다!
'''
