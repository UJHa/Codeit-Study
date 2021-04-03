'''
not yet solved
overtake time
1. card sort
2. card 정리하고 몇 장인지 리스트로 만들기
3. 이진탐색으로 정리한 리스트에서 찾기
4. 개수 몇장인지 정리한 리스트에서 뽑아서 정답 리스트에 어펜드
'''

def quicksort(list_a):

    if len(list_a) <= 1 : return list_a
    else:
        pivot = list_a[len(list_a)//2]
        less_arr, equal_arr, big_arr = [], [], []
        for i in list_a:
            if i < pivot: less_arr.append(i)
            elif i > pivot: big_arr.append(i)
            else: equal_arr.append(i)
        return quicksort(less_arr) + equal_arr + quicksort(big_arr)


def return_idx_bin_search(list_a, m, low, high):
    if low > high:
        return "a"

    mid = (low + high) // 2
    if list_a[mid] == m:
        return mid
    elif list_a[mid] > m:
        return return_idx_bin_search(list_a, m, low, mid - 1)
    else:
        return return_idx_bin_search(list_a, m, mid + 1, high)


def count_card():

    n = int(input())
    cards = list(map(int, input().split()))
    m = int(input())
    card_to_be_checked = list(map(int, input().split()))
    cards = quicksort(cards)
    #print(cards)
    card_num_list , numbers_of_card_list = [cards[0]], [1]
    num = cards[0]
    idx_numbers_of_card_list = 0

    for card in cards:
        if num < card:
            num = card
            card_num_list.append(num)
            numbers_of_card_list.append(1)
            idx_numbers_of_card_list += 1
        else: numbers_of_card_list[idx_numbers_of_card_list] += 1

    lencardlist = len(card_num_list)

    for checked_card in card_to_be_checked:
        check = return_idx_bin_search(card_num_list, checked_card, 0, lencardlist - 1)
        if type(check) == int:
            print(numbers_of_card_list[check], end=' ')
        else: print(0, end=' ')

    return 0


count_card()
