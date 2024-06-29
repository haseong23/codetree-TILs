n = int(input())
prod = 1

for i in range(1, 11, 1):
    prod *= i
    if prod >= n:
        print(i)
        break