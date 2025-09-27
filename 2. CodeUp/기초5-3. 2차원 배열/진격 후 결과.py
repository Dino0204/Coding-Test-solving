board = []

# 0 != n  장애물
# 0 < n   블럭 장애물
# 0 > n   구덩이 장애물
# 0 == n  평지

for i in range(10):
  board.append(list(map(int,input().split())))

mals = map(int, input().split())

for index ,mal in enumerate(mals):
  board[0][index] = mal

# print()
# for i in range(10):
#   for j in range(10):
#     print(board[i][j], end=" ")
#   print()

for i in range(10):
  if board[0][i]:
    survival = True
    
    for j in range(9, 0, -1):
      if board[j][i] > 0:
        print(f"{i+1} crash")
        survival = False
        break
      elif board[j][i] < 0:
        print(f"{i+1} fall")
        survival = False
        break
    
    if survival:
      print(f"{i+1} safe")
