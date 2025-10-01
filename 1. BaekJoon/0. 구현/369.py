# 3 6 9 가 포함 되어있으면 박수

n = int(input())

result = 0

for i in range(1,n+1):
  x = str(i)
  result += x.count('3')
  result += x.count('6')
  result += x.count('9')

print(result)

