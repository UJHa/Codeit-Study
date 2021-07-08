# 3번째 test case 성공 못함 
def make_str(str_):
    
    str_lst = []
    
    for i in range(len(str_)-1):
        
        str_value = str_[i] + str_[i+1]
        
        if str_value.isalpha():
            str_lst.append(str_[i] + str_[i+1])
    
    return str_lst

def solution(str1, str2):

    str1_lst = make_str(str1.lower())
    str2_lst = make_str(str2.lower())

    union_len = len(set(str1_lst).union(set(str2_lst)))
    inter_len = len(set(str1_lst).intersection(set(str2_lst)))

    if union_len == 0:
        union_len  = 1

    if inter_len == 0:
        inter_len = 1
        
    return round((inter_len/union_len)*65536)

solution("FRANCE", "french")
solution("handshake", "shake hands")
solution("aa1+aa2", "AAAA12")
solution("E=M*C^2", "e=m*c^2")
