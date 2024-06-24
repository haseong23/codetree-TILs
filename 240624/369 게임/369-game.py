n = int(input())

for i in range(1, n+1):
    i = str(i)
    l = len(i)
    for j in range(l):
        if i[j] == "3" or i[j] == "6" or i[j] == "9":
            print("0", end=" ")
        else:
            print(i, end=" ")