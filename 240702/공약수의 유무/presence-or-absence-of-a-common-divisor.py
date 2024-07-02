a, b = map(int, input().split())
is_flag = False

for i in range(a, b + 1):
    if 1920 % i == 0 and 2880 % i == 0:
        is_flag = True
if is_flag:
    print("1")
else:
    print("0")