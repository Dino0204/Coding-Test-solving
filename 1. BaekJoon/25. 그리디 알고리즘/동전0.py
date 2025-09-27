n , k = map(int,input().split())

dong = []

for i in range(n):
  dong .append(int(input()))

sum = 0

dong.reverse()

for i in dong:
  if k == 0:
    break
  sum += k//i
  k %= i


print(sum)
