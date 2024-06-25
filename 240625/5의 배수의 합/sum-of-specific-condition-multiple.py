a,b = map(int, input().split())

if a > b:
    a, b = b, a

sum_val = 0

for i in range(a, b+1):
    if i % 5 == 0:
        sum_val += i

print(sum_val)