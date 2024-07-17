n = int(input())

for i in range(n):
    print(' ' * (2*i), end='')
    print('* ' * (2 * (n-i) - 1))