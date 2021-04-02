'''
일단 가장 긴 랜선의 길이를  lanlen으로 설정, 개수 구하기
모자라면 두번째로 긴 랜선의 길이를 lanlen으로 설정, 개수 구하기, 이전 lanlen은 len_max로 설정
...이하 반복
1. 만약 랜선 개수가 넘어가면 lanlen~len_max 사이에서 이진 탐색으로 최대 길이 찾기
'''

def count_lan_num(lan_list, lanlen):
    count = 0
    for lan in lan_list:
        count += (lan // lanlen)
    #print("###{}".format(count))
    return count

def find_lanlen():

    k, n = map(int, input().split())
    lan_list = []
    lan_low = 0
    lan_max = 0
    for i in range(k):
        lan_list.append(int(input()))

    lan_list.sort(reverse=True)
    #print(lan_list)

    for lanlen in lan_list:
        if count_lan_num(lan_list, lanlen) < n:
            lan_max = lanlen

            if lan_max == lan_list[-1]:
                lan_low = 0
            continue
        elif count_lan_num(lan_list, lanlen) > n:
            lan_low = lanlen
            break
        else:
            return lanlen

    while lan_low <= lan_max:
        lan_length = (lan_max + lan_low)//2
        #print("lan_low{}, lan_max{}, lan_length{}".format(lan_low, lan_max, lan_length))

        if count_lan_num(lan_list, lan_length) < n:
            lan_max = lan_length - 1
        elif count_lan_num(lan_list, lan_length) > n:
            lan_low = lan_length + 1
        else:
            count = n
            while count == n:
                lan_length += 1
                count = count_lan_num(lan_list, lan_length)
            return lan_length - 1


print(find_lanlen())