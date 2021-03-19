# (2309) 일곱 난쟁이
def find_spies(smalls_heights):
    total = sum(smalls_heights)
    for spy1 in smalls_heights:
        for spy2 in smalls_heights:
            if spy1 == spy2:
                continue
            if total - spy1 - spy2 == 100:
                return [spy1, spy2]


smalls_heights = []
for i in range(9):
    smalls_heights.append(int(input()))

smalls_heights.sort()

# 숨어 들어온 스파이 2명 찾기
spies = find_spies(smalls_heights)

for height in smalls_heights:
    if height not in spies:
        print(height)