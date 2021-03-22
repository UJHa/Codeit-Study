# 숫자 빈도수

def frequency_num(n, d):
    d = str(d)
    count = 0
    for current in range(1, n+1):
        current = str(current)
        for index in range(len(current)):
            if d == current[index]:
                count += 1

    return count


end, digit = map(int, input().split())
print(frequency_num(end, digit))
# print(frequency_num(11, 1))
# print(frequency_num(100, 3))