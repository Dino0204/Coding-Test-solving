#회문 , 유사회문

T = int(input())

for k in range(T):
  str = input()
  end = len(str)-1  
  
  result = 0
  for i in range(end//2):
    # 좌우가 같지 않으면
    if end != 0 and str[i] != str[end - i]:
      leftPalin = 1
      rightPalin = 1
      
      # 왼쪽하나
      left = i + 1
      right = end - i
      while left < right:
        if str[left] != str[right]:
          leftPalin = 0
          break
        else:
          left += 1
          right -= 1

      # 오른쪽하나
      left = i
      right = end - i - 1
      while left < right:
        if str[left] != str[right]:
          rightPalin = 0
          break
        else:
          left += 1
          right -= 1
      
      # 문장 or 유사회문
      if leftPalin == 1 or rightPalin == 1:
        result = 1
        break
      else :
        result = 2
        break
  print(result)









