n = int(input())

for i in range(n):
    print(" " * 2*i, end="")
    print("* "* (2*(n-i)-1))

for i in range(n-1):
    print(" " * (-2*i+4), end="")
    print("* "*(2*i+3))