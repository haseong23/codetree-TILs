n = int(input())

for i in range(1, n+1):
    print("  "*(n-i), "@ "*i, sep="")

for i in range(1, n):
    print("@ "*(n-i))