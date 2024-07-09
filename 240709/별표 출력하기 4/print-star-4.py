n = int(input())

for i in range(n):
    print("* "*(n-i), end="")
    print()

for i in range(n-1):
    print("* "*(i+2), end="")
    print()