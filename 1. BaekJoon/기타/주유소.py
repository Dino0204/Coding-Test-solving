n = int(input())

# n-1개 2 3 1
cityKm = list(map(int,input().split()))

# n개 (1L == 1Km) 5 2 4 1 
oilCost = list(map(int,input().split()))

result = 0
minOilCost = oilCost[0]

# 총 기름 가격 : (도시 유가 * 기름 양)
# 산 기름 값보다 저렴한 기름 값이 나오는 거리만큼 기름을 삼
# 5 * 6 + 2 * 0 + 4 * 0 = 30 최악
# 5 * 2 + 2 * 3 + 4 * 1 = 20 평범
# 5 * 2 + 2 * 4 + 4 * 0 = 18 최소

for i in range(n-1):
  if(minOilCost > oilCost[i]): 
    minOilCost = oilCost[i]
  result += cityKm[i] * minOilCost

print(result)





