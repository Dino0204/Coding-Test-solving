n, m  = map(int,input().split())

snail_arr = [[0 for _ in range(m)] for _ in range(n)]
snail_arr[0][0] = n * m

num = n * m
i,j = 0,0
direction = 1

while num > 1:
  # right
  if direction == 1:
    if j + 1 >= m or (1 <= snail_arr[i][j + 1] <= n * m) :
      i += 1
      direction = 2
    else:
      j += 1
  # under
  elif direction == 2:
    if i + 1 >= n or (1 <= snail_arr[i + 1][j] <= n * m) :
      j -= 1
      direction = 3
    else:
      i += 1
  # left
  elif direction == 3:
    if j - 1 < 0 or (1 <= snail_arr[i][j - 1] <= n * m) :
      i -= 1
      direction = 4
    else:
      j -= 1
  # up
  elif direction == 4:
    if i - 1 < 0 or (1 <= snail_arr[i - 1][j] <= n * m) :
      j += 1
      direction = 1
    else:
      i -= 1
    
  num -= 1
  snail_arr[i][j] = num

for i in range(n):
  for j in range(m):
    print(snail_arr[i][j],end=" ")
  print()