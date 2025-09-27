crazy_arcade = []
players = []

pos = [
  [0, -1],
  [0, 1],
  [-1,0],
  [1, 0]
]

for i in range(10):
  crazy_arcade.append(list(map(int, input().split())))

result_ca = [[crazy_arcade[i][j] for j in range(10)] for i in range(10)]

n = int(input())

# 물줄기
def water_bomb(x, y):
  water_len = crazy_arcade[x][y]
  result_ca[x][y] = -2
  
  for p in pos:
    tmpx, tmpy = x, y
    x1, y1 = p
    
    for j in range(water_len):     
      tmpx += x1
      tmpy += y1
      if 0 <= tmpx < 10 and 0 <= tmpy < 10:
        # x = -1 장애물 (물줄기 멈춤)
        if crazy_arcade[tmpx][tmpy] == -1:
          break
        
        result_ca[tmpx][tmpy] = -2

# 물풍선
for i in range(10):
  for j in range(10):
    # x >= 1 물풍선 (숫자만큼 상하좌우)
    if crazy_arcade[i][j] >= 1:
      water_bomb(i, j)

# 플레이어 사망 판별
for player_cnt in range(1, n + 1):
  px, py = map(int, input().split())
  px -= 1
  py -= 1
  players.append([px, py])

  if result_ca[px][py] == 0:
    result_ca[px][py] = player_cnt

# 출력
for i in range(10):
  for j in range(10):
    print(result_ca[i][j], end=" ")
  print()

# 플레이어 사망 출력
print("Character Information")
for player_num in range(1, n+1):
  px, py = players[player_num - 1]
    
  if result_ca[px][py] >= 1:
    print(f"player {player_num} survive")
  else:
    print(f"player {player_num} dead")

