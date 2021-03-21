# 입력값 받기 
value = list(map(int, input().split())) 

def num_frequency(lst):
  count = 0

  for i in range(1,value[0]+1):
      nums = list(map(int, str(i)))  # 숫자의 자리수를 리스트로 쪼개어 변수에 담음. 

      for j in range(len(nums)):
          if nums[j] == value[1]:
              count +=1
              
  return count
  
print(num_frequency(value))
  
 
