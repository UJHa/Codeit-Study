def incorrect_person(height): 
              
    for i in range(len(height)):
        
        for j in range(i+1,len(height)):
            
            sum_height = sum(height)-height[-i]-height[-j]
            
            if sum_height == 100:
                
                return height[-i], height[-j]
            
                
height_lst = []

for i in range(9):
    height_lst.append(int(input()))
    
height_lst.sort()
            
incorrect_person_height = incorrect_person(height_lst)

# remove 를 사용하면 안됨!!!!!!
for height in height_lst:
    if height not in list(incorrect_person_height):
        print(height)
