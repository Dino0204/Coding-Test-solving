# T 파댕이 돌보는 시간
# N 사탕의 갯수
# F 사탕의 맛의 따라 울음을 멈추는 시간

t = int(input())
n = int(input())

candyF = list(map(int,input().split()))

print("Padaeng_i",end=" ")
if t <= sum(candyF):
  print("Happy")
else:
  print("Cry")