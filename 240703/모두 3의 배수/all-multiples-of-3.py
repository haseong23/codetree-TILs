is_multiple = 0

for _ in range(5):
    n = int(input())
    if n % 3 == 0:
        is_multiple += 1

if is_multiple == 5:
    print("1")
else:
    print("0")