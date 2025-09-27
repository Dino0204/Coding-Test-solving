# 창영 , 상덕
# 100 , 100
# 낮은 숫자가 낮은 경우에는 상대편 주사위 수 만큼 점수 - 
# 같은 경우에는 점수 - x

n = int(input())

CY = 100
SD = 100

for i in range(n):
  # CY dice / SD dice
  dice1, dice2 = map(int,input().split())
  
  if(dice1 > dice2):
    SD -= dice1
  elif(dice1 < dice2):
    CY -= dice2

print(CY)
print(SD)
