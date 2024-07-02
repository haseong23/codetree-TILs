a, b, c = map(int, input().split())
is_multiple = False

for i in range(a, b+1):
    if i % c == 0:
        is_multiple = True

if not(is_multiple):
    print("YES")
else:
    print("NO")