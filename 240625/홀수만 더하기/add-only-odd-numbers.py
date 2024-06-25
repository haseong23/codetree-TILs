n = int(input())
sum = 0

for i in range(n):
    if i % 3 == 0 and i % 2 == 1:
        sum += i

print(sum)