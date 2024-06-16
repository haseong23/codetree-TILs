temperature = int(input())
if temperature < 0:
    print("ice")
elif temperature >= 100:
    print("vapor")
else:
    print("water")