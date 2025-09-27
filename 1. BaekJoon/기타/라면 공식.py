# 물의 양  라면계수 * (라면 수 - 1) + 기본 물의 양

n = int(input())
for i in range(n):
  a, b,x = map(int, input().split())
  print(a * (x - 1) + b)