cnt = 0
sum_val = 0

while True:
    n = int(input())
    if n >= 20 and n <= 29:
        sum_val += n
        cnt += 1
    else:
        print(f"{sum_val/cnt:.2f}")
        break