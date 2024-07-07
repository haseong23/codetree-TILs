n = int(input())

# 줄바꿈을 위한 for
for i in range(n):
    # 별찍기를 위한 for
    for _ in range(n-i):
        for _ in range(n-i):
            print("*", end="")
        print(" ", end="")
    print()