n = int(input())
n = 2 * n + 2

for r in range(1, n):
    for c in range(1, n):
        if r % 2 == 1 or c % 2 == 1:
            print("* ", end="")
        else:
            print("  ", end="")
    print()