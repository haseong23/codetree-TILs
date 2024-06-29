# 변수 선언 및 입력
n = int(input())
prod = 1
x = 0

while True:
	# prod가 n이 될 때까지 2를 곱합니다.
	if n == prod:
		break

	prod *= 2
	x += 1

print(x)