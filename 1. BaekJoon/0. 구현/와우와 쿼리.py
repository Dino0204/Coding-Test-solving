# WOW의 개수를 알아내자

q = int(input())

for i in range(q):
  s = list(input())
  cnt = 0
  for j in range(len(s) - 2):
    if s[j] == "W" and s[j + 1] == "O" and s[j+2] == "W":
      cnt += 1
  print(cnt)