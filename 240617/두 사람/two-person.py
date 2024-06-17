a_age, a_sex = input().split()
b_age, b_sex = input().split()

a_age = int(a_age)
b_age = int(b_age)

if (a_age >= 19 and a_sex == 'M') or (b_age >= 19 and b_sex == 'M'):
    print(1)
else:
    print(0)