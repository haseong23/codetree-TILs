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

# # 정수 부분을 먼저 출력합니다.
# print(f"{a//b}.", end="")

# # a를 b로 나눈 나머지를 시작으로
# # 소수점 자리를 하나씩 계산합니다.
# a %= b
# for _ in range(20):
#     # 나머지에 10 곱한 값을 기준으로
#     # b로 나누었을 떄의 몫을 구해줍니다.
#     a *= 10
#     print(a // b, end="")

#     # a를 b로 나눈 나머지를 게속 갱신해줍니다.
#     a %= b