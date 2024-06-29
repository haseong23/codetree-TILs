n = int(input())
cnt = 0

while True:
    cnt += 1

    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1
    
    if n == 1:
        print(cnt)
        break