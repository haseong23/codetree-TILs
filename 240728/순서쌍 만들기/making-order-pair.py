n = int(input())

for i in range(n):
    for j in range(n):
        print('('+str(n-i)+','+str(n-j)+')', end=' ')
    print()