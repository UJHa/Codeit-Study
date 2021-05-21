# 전화번호 목록
# 정확성: 83.3
# 효율성: 16.7
# 합계: 100.0 / 100.0

def solution(phone_book):

    answer = True
    
    hash_map = {}
    
    for phone_number in phone_book:
        
        hash_map[phone_number] = hash(phone_number)
        
    for phone_number in phone_book:
        
        temp = ""
        
        for number in phone_number:
            
            temp += number
            
            if temp in hash_map and temp != phone_number:
                
                answer = False
                
    return answer
