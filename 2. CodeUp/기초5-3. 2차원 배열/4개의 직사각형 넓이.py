total_extent = 0
paper = [[0 for _ in range(100)] for _ in range(100)]

# 힌트) 0, 1을 활용하여 풀기, 넓이를 활용함
for _ in range(4):
  x1, y1, x2, y2 = map(int, input().split())

  for i in range(x1, x2):
    for j in range(y1, y2):
      paper[i][j] = 1

for i in range(100):
  for j in range(100):
    if paper[i][j] == 1:
      total_extent += 1

print(total_extent)