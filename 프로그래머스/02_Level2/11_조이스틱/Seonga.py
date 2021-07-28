# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 10:22:28 2021

@author: a0105
"""

def solution(name):
    
    # ord() 를 이용하여 알파벳 위치 인덱스 구할 수 있음. 
    # 상하조정: A부터 오름차순으로 알파벳을 찾거나 Z부터 내림차순으로 찾거나
    min_name = [min(ord(i) - ord("A"), ord("Z") - ord(i)+1) for i in name]  # 각 알파벳에 대한 최소 이동값 
    
    idx = 0
    answer = 0
    
    while True:
        
        answer += min_name[idx]  # 해당 위치의 상하조정 최소 이동값 할당
        
        min_name[idx] = 0  

        if sum(min_name) == 0: 
            break

        left, right = 1, 1
        
        while min_name[idx - left] == 0:  # 왼쪽으로 움직이면서 최소 이동값 
            left += 1
        
        while min_name[idx + right] == 0:  # 오른쪽으로 움직이면서 최소 이동값
            right += 1
            
        if left < right:  # left 가 right 보다 작다는 것을 먼저 비교해야함. 아니면 test11 에서 실패 
            idx += -left
            
        else:
            idx += right
            
        answer += min(left, right)
        
    return answer
