'''

'''
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
    card = list(map(int, input().split()))
    m = int(input())
    card_to_be_checked = list(map(int, input().split()))
    card.sort()
    #print(card)

    for checked_card in card_to_be_checked:
        count = 0
        right_check = 1
        left_check = 1

        #print(checked_card)

        if type(return_idx_bin_search(card, checked_card, 0, n - 1)) == int:
            count += 1
            idx = return_idx_bin_search(card, checked_card, 0, n - 1)
            #print(idx)
            while idx - left_check > -1 and left_check != 0:
                if card[idx - left_check] == checked_card:
                    count += 1
                    left_check += 1
                else: left_check = 0
            while idx + right_check < n and right_check != 0:
                if card[idx + right_check] == checked_card:
                    count += 1
                    right_check += 1
                else: right_check = 0

            print(count, end=' ')

        else: print(count, end=' ')

        #print("#####")


count_card()


