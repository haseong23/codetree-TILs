n = int(input())
mok = n
cnt = 0

for i in range(1, n):
    mok //= i
    cnt += 1
    if mok <= 1:
        print(cnt)
        break