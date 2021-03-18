def partition():

    a, b, c, n = map(int, input().split())

    case_a = n // a
    case_b = n // b

    for i in range(case_a + 1):
        for j in range(case_b + 1):
            if (n - a*i - b*j) % c == 0:
                return 1
    return 0

print(partition())