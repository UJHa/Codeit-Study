new_list = [] 
for i in range(1, 6): 
    w = input() 
    if "FBI" in w: 
        new_list.append(i) 
if new_list: 
    print(*new_list) 
else: 
    print("HE GOT AWAY!")
