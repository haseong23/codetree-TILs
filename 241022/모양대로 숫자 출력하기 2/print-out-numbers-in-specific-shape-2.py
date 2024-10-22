n = int(input())
num_arr = [2, 4, 6, 8]
cnt = len(num_arr)

for i in range(n):
    row = [num_arr[(j + i) % cnt] for j in range(n)]
    print(" ".join(map(str, row)))