n,m = map(int,input().split())

snail_arr = [[0 for _ in range(m)] for _ in range(n)]

directions = [[0,0],[0,m-1],[n-1,m-1],[n-1,0]]

def fill_snail(direction, p):
  i,j = directions[direction - 1][0] , directions[direction - 1][1]
  num = 1
  
  if p == "AZ":
    num = 1
  elif p == "ZA":
    num = n * m

  snail_arr[i][j] = num

  while True:
    
    if p == "AZ" and num >= n * m:
      break
    elif p == "ZA" and num <= 1:
      break
    
    prevI,prevJ = i,j
    
    # right
    if direction == 1:
      if j + 1 >= m or (1 <= snail_arr[i][j + 1] <= n * m):
        if i + 1 < n:
          i += 1
        direction = 2
      else:
        j += 1
    # under
    elif direction == 2:
      if i + 1 >= n or (1 <= snail_arr[i + 1][j] <= n * m):
        if j - 1 >= 0:
          j -= 1
        direction = 3
      else:
        i += 1
    # left
    elif direction == 3:
      if j - 1 < 0 or (1 <= snail_arr[i][j - 1] <= n * m):
        if i - 1 >= 0:
          i -= 1
        direction = 4
      else:
        j -= 1
    # up
    elif direction == 4:
      if i - 1 < 0 or (1 <= snail_arr[i - 1][j] <= n * m):
        if j + 1 < m:
          j += 1
        direction = 1
      else:
        i -= 1
    
    if prevI != i or prevJ != j:
      if p == "AZ":
        num += 1
      elif p == "ZA":
        num -= 1
    snail_arr[i][j] = num

# 시작 위치, 차순
# 102
# 000
# 403 , AZ / ZA
fill_snail(4,"ZA")

for i in range(n):
  for j in range(m):
    print(snail_arr[i][j],end=" ")
  print()