c, n = input().split(" ")
n = int(n)

if c == "A":
    for i in range(n):
        print(i+1, end=" ")
        i += 1
elif c == "D":
    for i in range(n):
        print(n-i, end=" ")
        i += 1