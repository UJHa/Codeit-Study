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

    if len(str1_lst) > len(str2_lst):
        inter_lst = [str1_lst.remove(x) for x in str2_lst if x in str1_lst]
    else:
        inter_lst = [str2_lst.remove(x) for x in str1_lst if x in str2_lst]

    union_len = len(str1_lst + str2_lst)

    if union_len == 0:
        return 65536
        
    return int((len(inter_lst)/union_len)*65536)

solution("FRANCE", "french")
solution("handshake", "shake hands")
solution("aa1+aa2", "AAAA12")
solution("E=M*C^2", "e=m*c^2")
