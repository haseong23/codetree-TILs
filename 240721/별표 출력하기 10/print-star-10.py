n = int(input())

for i in range(1, n*2+1):
    if i % 2 == 1:
        print("* "*(int(i/2)+1))
    else:
        print("* "*(int(n-(i/2))+1))