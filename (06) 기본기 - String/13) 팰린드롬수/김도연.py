while(True):
    i = str(input())
    mid = len(i)//2
    
    if i == '0':
        break
        
    elif len(i)%2 !=0 :
        i=i.replace(i[mid],'',1)
      
    if len(i)%2 ==0: 
        if i[:mid] == i[:mid-1:-1]:
            print("yes")
        else:
            print('no')
