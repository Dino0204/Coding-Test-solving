n = int(input())
grid = [[0 for _ in range(n)] for _ in range(n)]

for h in range(n):
  grid[h][0] = int(input())

for i in range(1,n):
  for j in range(i):
    # 이 줄에 다음거 = 이 줄에 지금거 - 전 줄에 위거
    grid[i][j+1] = grid[i][j] - grid[i-1][j]

for i in range(n):
  for j in range(i+1):
    print(grid[i][j],end=" ")
  print()
