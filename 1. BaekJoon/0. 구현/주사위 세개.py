# 같은 눈이 3개 나오면 10000원+(같은 눈)*1000원
# 같은 눈이 2개 나오면 1000원+(같은 눈)*100원
# 모두 다른 눈이 나오면 (가장 큰 눈)*100원

a, b, c = map(int, input().split())

if a == b == c:
  print(10000 + a * 1000)
elif a == b or a == c:
  print(1000 + a * 100)
elif b == c:
  print(1000 + b * 100)
else:
  print(max(a, b, c) * 100)
