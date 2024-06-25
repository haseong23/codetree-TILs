n = int(input())
sum_val = 0

for _ in range(n):
    i = int(input())
    sum_val += i

print(f"{sum_val} {sum_val/n:.1f}")