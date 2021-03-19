# (13417)카드 문자열
def sort_by_dictionary(cards):
    temp_word = ''

    for i in range(len(cards)):
        if i == 0: # 첫 번째 문자에 대한 예외 처리
            temp_word = cards[i]
        else:
            if temp_word[0] < cards[i]:
                temp_word += cards[i]
            else:
                temp_word = cards[i] + temp_word

    return temp_word


input_count = int(input())

sort_string_list = []

for i in range(input_count):
    char_count = int(input())
    char_list = list(map(str, input().split()))

    sort_string_list.append(sort_by_dictionary(char_list))

for s in sort_string_list:
    print(s)