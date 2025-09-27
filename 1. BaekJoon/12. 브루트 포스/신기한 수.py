n = int(input())
result = 0

for i in range(1, n + 1):
  x = list(map(int, list(str(i))))
  result += not i % sum(x) 

print(result)