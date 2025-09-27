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

def isLiving(x, y):
  life_cnt = 0
  for p in pos:
    x1, y1 = p
    
    if 0 <= x + x1 <= 24 and 0 <= y + y1 <= 24:
      if life_game[x + x1][y + y1]:
        life_cnt += 1
  return life_cnt

for i in range(25):
  life_game.append(list(map(int, input().split())))

next_life_game = [[life_game[i][j] for j in range(25)] for i in range(25)]

# 생명이 없는 칸
  # 3개의 생명 -> 생명 탄생
# 생명이 있는 칸
  # 4개 이상 or 1개 이하의 생명 -> 생명 사망

for i in range(25):
  for j in range(25):
    life_cnt = isLiving(i, j)
    
    if life_game[i][j] == 0:
      if life_cnt == 3:
        next_life_game[i][j] = 1
    
    elif life_game[i][j] == 1:
      if life_cnt <= 1 or life_cnt >= 4:
        next_life_game[i][j] = 0

for i in range(25):
  for j in range(25):
    print(next_life_game[i][j], end=" ")
  print()