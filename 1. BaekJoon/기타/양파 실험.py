# 칭찬 양파, 비난 양파
# A, B만큼 자라남 (A < B)

n,a,b = map(int,input().split())

goodOnion = 1
badOnion = 1

for i in range(n):
  goodOnion += a
  badOnion += b
  
  if goodOnion < badOnion:
    temp = goodOnion
    goodOnion = badOnion
    badOnion = temp
  elif goodOnion == badOnion:
    badOnion -= 1

print(goodOnion, badOnion)