n = int(input())

print("* " * (n))

for r in range(1, n+1):
    for c in range(1, n+1):
        if c % 2 == 0 and c > r:
            print("* ", end="")
        else:
            print("  ", end="")
    print()