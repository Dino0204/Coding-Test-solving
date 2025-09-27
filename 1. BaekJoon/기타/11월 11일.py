#  m월 m일의 m일전의 날짜

# 1,2,3,4,5,6,7,8,9,10,11,12
month = [31,28,31,30,31,30,31,31,30,31,30,31]

t = int(input())

for i in range(t):
  y,m = map(int,input().split())
  
  if ((y % 100 != 0) and (y % 4 == 0)) or (y % 400) == 0:
    month[1] = 29
  else:
    month[1] = 28
  
  if m - 1 == 0:
    print(y-1,12,month[m - 2])
  else:
    print(y,m - 1,month[m - 2])
