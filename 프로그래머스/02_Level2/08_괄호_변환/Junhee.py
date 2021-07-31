def solution(p):
    """입력받은 문자열을 균형잡히고 올바르게 변환하여 반환하는 함수  
    
    Args:
        p: 균형잡힌 문자열 
        u: 최소 길이로 균형잡힌 문자열
        v: u를 제외한 나머지 문자열
        new_u: u의 앞뒤를 제거하고 모든 괄호를 뒤집은 문자열 

    Returns:
        균형잡히고 올바른 문자열  
    """
    if not p or check_str(p) == True:
        return p 
    
    u, v = divide_str(p)
    if check_str(u) == True:
        u += solution(v)  
        return u  
    else:
        new_u = reverse_str(u[1:-1])  
        return '(' + solution(v) + ')' + new_u  


def divide_str(w):
    """문자열 w를 u와 v로 분리하는 함수

    Args:
        w: 균형잡힌 문자열
        u: w의 좌측부터 최소 길이의 균형잡힌 문자열
        v: w에서 u를 제외한 나머지 문자열
        check: 최소 길이를 검증하기 위한 변수 

    Returns:
        u와 v를 Tuple 형태로 반환 
    """
    check = 0 
    u = v = ""

    for i, c in enumerate(w):
        if c == '(':
            check += 1
        else:
            check -= 1
        u += c
        if check == 0 and i+1 < len(w): 
            v = w[i+1:] 
            break

    return (u, v)


def check_str(w):
    """문자열 w가 올바른지 확인하는 함수
    
    Args:
        w: 균형잡힌 문자열  
        check: 문자열이 올바른지 검증하기 위한 변수 

    Returns:
        True: 올바른 문자열
        False: 올바르지 않은 문자열 
    """
    check = 0
    
    for c in w:
        if c == '(':
            check += 1
        else:
            check -= 1
        if check < 0:
            return False
    
    if check == 0:
        return True
    else:
        return False

def reverse_str(w):
    """문자열 w의 괄호 방향을 뒤집는 함수
    
    Args: 
        w: 균형잡힌 문자열
        s: 괄호의 방향을 전부 뒤집은 문자열

    Returns:
        괄호가 전부 뒤집힌 문자열   
    """
    s = ""

    for c in w:
        if c == '(': 
            s += ')'
        else:
            s += '('     
    
    return s 

