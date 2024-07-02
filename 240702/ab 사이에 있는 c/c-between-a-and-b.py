a, b, c = map(int, input().split())
is_even = False

for i in range(a, b + 1):
    if i % c == 0:
        is_even = True

if is_even:
    print("YES")
else:
    print("NO")