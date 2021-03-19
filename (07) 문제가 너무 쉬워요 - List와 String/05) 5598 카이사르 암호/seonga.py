from string import ascii_uppercase
# from string import ascii_lowercase # A-Z 소문자 생성하는 모듈

low_aplha = list(ascii_uppercase)  # A-Z대문자 자동생성 
low_aplha_revise = low_aplha[3:len(low_aplha)]+low_aplha[0:3]  # 카이사르 생성 

# 입력받기 
word = input()

word_index = [low_aplha_revise.index(word_alpha) for word_alpha in word]
result = ''.join([low_aplha[word_index_value] for word_index_value in word_index])

print(result)
