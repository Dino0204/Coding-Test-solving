n = int(input())
ballColor = list(input())

# 인수로 받은 공 기준 색깔 대로 역순과 정순을 판단하여 작은값을 반환하는 함수
def Ball(thisColor,ballColor):
  
  cntI = 0     # 공 총 변경 횟수
  cntTemp = 0  # 기준 색깔과 다른 공을 만날때까지의 공 뭉탱이

  # 역순으로 공 탐색
  for i in range(n-1, -1 , -1):
    if thisColor != ballColor[i]:
      cntTemp += 1
    
    if thisColor == ballColor[i]:
      cntI += cntTemp
      cntTemp = 0
  
  cntJ = 0
  cntTemp = 0
  
  for i in range(n):
    if thisColor != ballColor[i]:
      cntTemp += 1
    
    if thisColor == ballColor[i]:
      cntJ += cntTemp
      cntTemp = 0
  
  #print(f"역순 : {cntI} | 정순 : {cntJ}")
  
  if cntI <= cntJ:
    return cntI
  else:
    return cntJ


cntA = Ball('R', ballColor)
cntB = Ball('B', ballColor)

#print(f'{cntA} {cntB}')

# 두 색깔중 최솟값 찾기
if cntA <= cntB:
  print(cntA)
else:
  print(cntB)
