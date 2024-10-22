n = int(input())
num_arr = [2, 4, 6, 8]
length = len(num_arr)

for i in range(n):
    row = []
    for j in range(n):
        row.append(num_arr[(i + j) % length])
    print(" ".join(map(str, row)))