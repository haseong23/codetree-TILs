n = int(input())
is_hss = False

for i in range(2, n):
    if n % i == 0:
        is_hss = True

if is_hss:
    print("C")
else:
    print("N")