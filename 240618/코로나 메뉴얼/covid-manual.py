a_flag1, a_flag2 = input().split()
b_flag1, b_flag2 = input().split()
c_flag1, c_flag2 = input().split()

a_flag2 = int(a_flag2)
b_flag2 = int(b_flag2)
c_flag2 = int(c_flag2)

cnt = 0

if a_flag1 == 'Y' and a_flag2 >= 37:
    cnt += 1

if b_flag1 == 'Y' and b_flag2 >= 37:
    cnt += 1

if c_flag1 == 'Y' and c_flag2 >= 37:
    cnt += 1

if cnt >= 2:
    print("E")
else:
    print("N")