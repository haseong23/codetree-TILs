a, b, c = map(int, input().split())
min = a

if b <= min:
    min = b
if c <= min:
    min = c

if min == a:
    print(1, end = " ")
else:
    print(0, end = " ")

if a == b and b == c:
    print(1)
else:
    print(0)