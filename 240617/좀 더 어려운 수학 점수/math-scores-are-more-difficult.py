a_math, a_eng = map(int, input().split())
b_math, b_eng = map(int, input().split())

if b_math > a_math:
    print("B")
elif a_math > b_math:
    print("A")
elif b_eng > a_eng:
    print("B")
elif a_eng > b_eng:
    print("A")