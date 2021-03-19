# (1065)한수 구하기
def is_hansu(num):
    num = str(num)
    if len(num) == 1 or len(num) == 2:
        return True
    else:
        common_difference = int(num[0]) - int(num[1])
        for i in range(len(num) - 1):
            if common_difference != int(num[i]) - int(num[i + 1]):
                return False
        return True


x = int(input())

count = 0
for i in range(1, x + 1):
    if is_hansu(i):
        count += 1

print(count)