h, w = map(int, input().split())
b = (10000*w)//(h**2)
if(b >= 25):
    print(b, "Obesity", sep="\n")
else:
    print(b)