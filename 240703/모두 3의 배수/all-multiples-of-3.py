is_multiple = False

for _ in range(5):
    n = int(input())
    if n % 3 == 0:
        is_multiple = True

if is_multiple:
    print("1")
else:
    print("0")