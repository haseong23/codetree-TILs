a, b, c = map(int, input().split())
min = a

if b < min:
    min = b

if c < min:
    min = c

print(min)