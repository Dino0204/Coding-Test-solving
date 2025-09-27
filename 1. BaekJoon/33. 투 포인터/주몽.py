# 재료 갯수
n = int(input())

# 고유번호의 합
m = int(input())

# 재료마다의 고유번호
inherenceList = list(map(int,input().split()))

inherenceList.sort()

#print(inherenceList)

totalArmors = 0
left = 0
right = n - 1


while True:
  
  # 종료조건
  if left >= right:
    break
  
  armor = inherenceList[left] + inherenceList[right]
  
  if armor == m:
    totalArmors += 1
    left += 1
    
  elif armor > m:
    right -= 1
    
  elif armor < m:
    left += 1

print(totalArmors)