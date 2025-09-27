n, k = map(int, input().split())

balls = 0

# 2. 각 바구니에는 1개 이상의 공이 들어 있어야 한다.
for i in range(1, k + 1):
  balls += i

# 2-1. 그렇지 못한 경우
if balls > n:
  print(-1)
  exit()

# 2-2. 그런 경우
else:
  n -= balls

  basket = [i for i in range(1, k + 1)]
  length = len(basket)
  
  while n > 0:
    n -= 1
    
    if length - 1 < 0:
      length= len(basket)
    length -= 1
    
    basket[length] += 1
print(max(basket) - min(basket))