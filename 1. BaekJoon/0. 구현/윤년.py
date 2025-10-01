year = int(input())

# 윤년 조건 4의 배수 이면서 100의 배수가 아니거나 400의 배수인 경우
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
  print(1)
else:
  print(0)