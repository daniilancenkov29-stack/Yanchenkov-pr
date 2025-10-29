A = int(input("A: "))
B = int(input("B: "))
num = A
while num <= B:
    count = num - A + 1
    i = 0
    while i < count:
        print(num)
        i += 1
    num += 1