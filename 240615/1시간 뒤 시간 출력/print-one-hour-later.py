h, m = map(int, input().split(":"))
h = h + 1
# h가 23이상도 가능하다면 모듈러 연산까지 적용해야 함.
print(h, m, sep=":")