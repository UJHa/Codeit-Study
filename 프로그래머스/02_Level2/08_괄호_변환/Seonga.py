
# 문자열 분리
# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 
# 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
def uv_divide(p):
    
    num = 0
    
    u = v = ""
    
    for i, value in enumerate(p):
        
        if value == "(":
            num += 1
            
        else:
            num -= 1
        
        u += value # u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며
        
        if num == 0 and i+1 < len(p):
            v = p[i+1:]  # v는 빈 문자열이 될 수 있습니다. 
            break
        
    return (u, v) 
    
# 문자열이 올바른지 확인 
def check_str(value):
    
    temp = 0
    
    for v in value:
        
        if v == "(":
            temp += 1
            
        else:
            temp -= 1
        
        if temp < 0:
            return False
            
    if temp == 0:
        return True
    
    else:
        return False

            
# u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
def reverse_str(p):
    
    s = ""
    
    for c in p:
        if c == "(":
            s += ")"
        else:
            s += "("
    
    return s

def solution(p):
    
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
    if not p or check_str(p) == True:
        return p 
    
    u, v = uv_divide(p) # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
    
    if check_str(u) == True:  # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
        u += solution(v)
        return u

    # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
    # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
    # 4-3. ')'를 다시 붙입니다. 
    # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
    else:
        new_u = reverse_str(u[1:-1])  
        return '(' + solution(v) + ')' + new_u  
