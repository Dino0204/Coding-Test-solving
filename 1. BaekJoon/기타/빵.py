# 즉시  품절
# 사려면 빵 오기 전 가게에서 대기 , 또는 오는 순간에 정확히 와야함
# N개의 가게 
# 현재 위치 ~ 가게까지 걸리는 시간, KOI빵이 가게에 올 때까지 남은시간
# 가장 빨리 몇 분 뒤에 빵을 구할 수 있는지 구하는 프로그램

n = int(input())
koiList = []

for i in range(n):
  store_time, bread_time = map(int,input().split())
  
  if bread_time - store_time >= 0:
    koiList.append(bread_time)

koiList.sort()

if len(koiList) > 0:
  print(min(koiList))
else:
  print(-1)