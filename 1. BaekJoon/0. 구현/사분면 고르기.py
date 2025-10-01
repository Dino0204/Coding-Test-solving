x = int(input())
y = int(input())

# 1사분면 양수,양수 | 2사분면 음수,양수 | 3사분면 음수,음수 | 4사분면 양수,음수
if x > 0 and y > 0:
  print(1)
elif x < 0 and y > 0:
  print(2)
elif x < 0 and y < 0:
  print(3)
else:
  print(4)
