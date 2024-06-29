x = 1

n = int(input())

while True:
    if 2 ** x != n:
        x += 1
    else:
        print(x)
        break