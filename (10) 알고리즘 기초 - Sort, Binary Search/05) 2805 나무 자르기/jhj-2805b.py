'''
1.나무 높이 정렬
2.나무 높이 차 리스트 만들기
3.standardn = diff[0]1 + diff[1]2 + diff[2]*3 ~
4.standard(n-1) < m < standard(n)이면 standard(n-1)부터 1씩 늘려가면서 m 지점 찾기
'''

def cut_tree():

    n, m = map(int,input().split())
    list_tree = list(map(int, input().split()))

    if n == 1:
        print(list_tree[0] - m)
        return 0

    else:
        list_tree.sort(reverse=True)
        list_diff = []
        standard_count = 0
        height_minus = 0
        standard = 0

        for i in range(n-1):
            list_diff.append(list_tree[i] - list_tree[i+1])

        #print(list_diff)

        while standard + list_diff[standard_count]*(standard_count + 1) < m:
            height_minus += list_diff[standard_count]
            standard += list_diff[standard_count]*(standard_count + 1)
            standard_count += 1

        #print(standard_count)

        for diff in range(list_diff[standard_count]):
            standard += (standard_count + 1)*1
            height_minus += 1
            if standard >= m:break

        print(list_tree[0] - height_minus)

        return 0


cut_tree()