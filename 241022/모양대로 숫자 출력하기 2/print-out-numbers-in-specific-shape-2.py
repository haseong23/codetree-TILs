n = int(input())
num_arr = [2, 4, 6, 8]
cnt = 0

for i in range(n):
    row = []
    for j in range(n):
        row.append(num_arr[cnt % 4])
        cnt += 1
    print(" ".join(map(str, row)))