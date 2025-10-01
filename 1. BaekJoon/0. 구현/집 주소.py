# 집 주소를 나타내는 호수판

# 숫자 사이, 양쪽 끝 여백 = 1cm
# 1 = 2cm
# 0 = 4cm
# Others = 3cm


while True:
  homeNum = str(input())
  
  if homeNum == '0':
    break
  
  homeNum = list(homeNum)
  homeCount = 0
  
  for i in homeNum:
    if i == '0':
      homeCount += 4
    elif i == '1':
      homeCount += 2
    else:
      homeCount += 3
  print(homeCount + len(homeNum) + 1)