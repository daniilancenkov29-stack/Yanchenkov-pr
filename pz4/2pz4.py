N = int(input("N: "))
K = int(input("K: "))
quotient = 0
temp = N
while temp >= K:
    quotient += 1
    temp -= K
print("Частное:", quotient)
print("Остаток:", temp)