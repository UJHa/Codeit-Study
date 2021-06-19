# 전화번호 목록
# 정확성: 83.3
# 효율성: 16.7
# 합계: 100.0 / 100.0

def solution(phone_book):

    answer = True
    
    hash_map = {}  # 전화번호를 담을 딕셔너리 
    
    for phone_number in phone_book:
        
        hash_map[phone_number] = hash(phone_number)  # 전화번호에 해당하는 hash 값을 키로 value를 phone number로 딕셔너리 생성
        
    for phone_number in phone_book: 
        
        temp = ""
        
        for number in phone_number:
            
            temp += number  # 접두사가 있는지 확인 
            
            # 딕셔너리 내에 접두사가 있으면 False 반환 
            if temp in hash_map and temp != phone_number:
                
                answer = False
                
    return answer
