n = int(input())

for i in range(1, n*2+1):
    if i % 2 == 1:
        print("* " * (n-int(i/2)))
    else:
        print("* " * int(i/2))