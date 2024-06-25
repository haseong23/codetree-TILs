n = int(input())
sum = 0

for _ in range(n):
    i = int(input())
    if i % 3 == 0 and i % 2 == 1:
        sum += i

print(sum)