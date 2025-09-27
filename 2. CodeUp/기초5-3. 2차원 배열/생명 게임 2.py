life_game = []

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

a, b = map(int, input().split())

def isLiving(x, y):
  life_cnt = 0
  for p in pos:
    x1, y1 = p
    
    if 0 <= x + x1 < a and 0 <= y + y1 < b:
      if life_game[x + x1][y + y1]:
        life_cnt += 1
  return life_cnt

x, y, z = map(int, input().split())

for _ in range(a):
  life_game.append(list(map(int, input().split())))

next_life_game = [[life_game[i][j] for j in range(b)] for i in range(a)]

k = int(input())

for _ in range(k):
  for i in range(a):
    for j in range(b):
      life_cnt = isLiving(i, j)
      
      # 주변에 x개의 생명 존재 시 생명 탄생
      if life_game[i][j] == 0:
        if life_cnt == x:
          next_life_game[i][j] = 1
      
      # 주변에 z개 이상의 생명 존재 시 생명 사망 | 주변에 y개 이상 생명 존재 시 생명 생존
      elif life_game[i][j] == 1:
        if z <= life_cnt or life_cnt < y:
          next_life_game[i][j] = 0
  # 복사
  life_game = [[next_life_game[i][j] for j in range(b)] for i in range(a)]

for i in range(a):
  for j in range(b):
    print(next_life_game[i][j], end=" ")
  print()

