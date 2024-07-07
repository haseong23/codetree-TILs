n = int(input())

for i in range(n):
    for _ in range(i*2+1):
        print("*", end="")
    print()