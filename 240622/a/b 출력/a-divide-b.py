a, b = map(int, input().split())

# 손으로 나눗셈 하듯이 몫만을 찍어내면 됌. 단, 소수점도 넣어줘야겠지
i = 0
for i in range(21):
    m = a // b
    n = a % b
    a = n * 10

    print(m, end="")
    if i==0:
        print(".", end="")