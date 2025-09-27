n = int(input())

cnt = 1
lPoint = 1
rPoint = 2
result = lPoint + rPoint

while True:
  if rPoint <= lPoint:
    break

  # 더한 값이 n과 같을 때
  if result == n:
    # print(f"=|result + {lPoint} + {rPoint} =  {result}")
    cnt += 1
    rPoint += 1
    result += rPoint
    
  # 더한 값이 n보다 클 때
    # print(f"b|result + {rPoint} + {rPoint} =  {result}")
  elif result >n:
    
    result -= lPoint
    lPoint += 1
  
  # 더한 값이 n보다 작을 때
  elif result < n:
    # print(f"s|result + {lPoint} + {rPoint} =  {result}")
    rPoint += 1 #누적 합
    result += rPoint #합 갱신


print(cnt)