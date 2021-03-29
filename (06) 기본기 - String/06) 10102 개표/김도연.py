num = int(input())
vote = list(input())

A = 0
B = 0

for num in vote:
    if num == 'A':
        A += 1
    else:
        B += 1

if A == B:
    print("Tie")
elif A > B:
    print("A")
else:
    print("B")
