n = int(input())
print('*' * (n*2))

for i in range(1, n):
    print('*' * (n-i), end='')
    print('  ' * i, end='')
    print('*' * (n-i), end='')
    print()