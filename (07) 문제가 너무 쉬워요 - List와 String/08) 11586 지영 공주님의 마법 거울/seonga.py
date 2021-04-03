
n = int(input())
arr = [list(input()) for _ in range(n)]  
emotion = int(input())


import copy

i = 0
j = len(arr)-1

temp = copy.deepcopy(arr)


if emotion == 1:
    for i in range(len(arr)):
        print(''.join(arr[i]))    
    
elif emotion == 2:
    

    while i < len(arr)-(n//2):
            
        for row in range(len(arr)):
            
            arr[row][i] = temp[row][j]
            arr[row][j] = temp[row][i]
                    
        i += 1
        j -= 1
      
    for i in range(len(arr)):
        print(''.join(arr[i]))
            
elif emotion == 3:
    while i < len(arr)-(n//2):
       
        arr[i] = temp[j]
        arr[j] = temp[i]
                
        i += 1
        j -= 1
        
    for i in range(len(arr)):
        print(''.join(arr[i]))
