# O-표기법(빅 오)
# 1 ~ 7까지 함수의 조건을 만족하는지 확인한다 
# 1. f(n) = 7n + 7
# 2. c = 8
# 3. n0 = 1

# f(1) = 14
# 8 * 1 = 8

a1, a0 = map(int,input().split())
c = int(input())
n0 = int(input())


isTrue = True

for i in range(n0,101):
  fn = (a1 * i) + a0
  gn = c * i
  
  # print(f"{fn} ? {gn}")
  
  if fn > gn:
    isTrue = False
    print(0)
    break


if isTrue:
  print(1)