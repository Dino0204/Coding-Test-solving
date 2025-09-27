eightBit = list(map(int, input().split()))

canRead = True

for i in range(8):
    if eightBit[i] == 9:
        canRead = False

print("S" if canRead else "F")
