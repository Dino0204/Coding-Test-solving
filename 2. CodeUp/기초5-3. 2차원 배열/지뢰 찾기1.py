mines = []

pos = [
  [-1,-1],
  [0, -1],
  [1, -1],

  [1, 1],
  [0, 1],
  [-1,1],
  
  [-1,0],
  [1, 0]
]

cnt = 0

for i in range(9):
  mines.append(list(map(int, input().split())))

r , c = map(int, input().split())

r -= 1
c -= 1

if mines[r][c] == 1:
  print(-1)
  exit()

for i in range(8):
  r1 , c1 = pos[i]
  
  if 0 <= r + r1 < 9 and 0 <= c + c1 < 9 and mines[r + r1][c + c1] == 1:
    cnt += 1
print(cnt)