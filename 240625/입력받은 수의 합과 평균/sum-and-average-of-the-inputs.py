n = int(input())
cnt = 0
sum_val = 0

for _ in range(n):
    i = int(input())
    sum_val += i
    cnt += 1

print(f"{sum_val} {sum_val/cnt:.1f}")