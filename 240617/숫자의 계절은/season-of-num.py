m = int(input())

# 수직선을 생각하면서 조건의 순서를 생각해야 한다.
if m >= 12 or m <= 2:
	print("Winter")
elif m <= 5:
	print("Spring")
elif m <= 8:
	print("Summer")
else:
	print("Fall")