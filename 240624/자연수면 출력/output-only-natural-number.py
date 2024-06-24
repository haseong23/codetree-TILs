a, b = map(int, input().split())

# 1로 나눈 나머지가 0이라면 자연수이다.
if a < 0:
    print("0")
elif a % 1 == 0:
    for _ in range(b):
        print(a, end="")