aCards = list(map(int,input().split()))
bCards = list(map(int,input().split()))

# 각각의 점수
aWinCnt = 0
bWinCnt = 0

# 누가 이겼는지 초기값이 그대로 남아있을 경우 모든판이 비긴 것
whoIsWin = 2

# 0 ~ 9 까지의 섞여있는 카드 (게임 도중에는 바뀌지 않음)
# 이길 시 3점 / 비길 시 각각 1점 / 질 시 0점
# 만약 총점이 같을 경우 마지막에 이긴 사람을 승자로 정하고 승부가 나지 않는 경우(모든 게임을 비긴 경우)에는 비겼다고 한다.

for i in range(10):
  if aCards[i] > bCards[i]:
    whoIsWin = 0
    aWinCnt += 3
  elif aCards[i] < bCards[i]:
    whoIsWin = 1
    bWinCnt += 3
  else:
    aWinCnt += 1
    bWinCnt += 1

# 점수 출력
print(f"{aWinCnt} {bWinCnt}")

# 승리 조건
if aWinCnt > bWinCnt:
  print("A")
elif aWinCnt < bWinCnt:
  print("B")
else:
  if whoIsWin == 0:
    print("A")
  elif whoIsWin == 1:
    print("B")
  else :
    print("D")