while(True):
    i = str(input())
    mid = len(i)//2
    if i == '0':break #종료조건
    elif len(i)%2 !=0 : #홀수인경우
        i=i.replace(i[mid],'',1) #홀수인경우 : 정가운데 수를 날려준다.
    if len(i)%2 ==0: #짝수인경우 
        if i[:mid] == i[:mid-1:-1] : print("yes")
        else : print('no')
