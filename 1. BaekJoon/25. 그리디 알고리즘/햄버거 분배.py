n, k = map(int, input().split())
hamburgers = list(input())
eat = False

for i in range(n):
  if(hamburgers[i] == "H"):
    for j in range(i - 1, i - k - 1, -1):
      try:
        if(hamburgers[j] == "P"):
          hamburgers[i] = "E"
          print(f"{i}, {j}, {hamburgers[j]}")
          eat = True
          break
      finally:
        print()

    if (eat): 
      eat = False 
      continue
  
    for j in range(i + 1, i + k + 1, +1):
      try:
        if(hamburgers[j] == "P"):
          hamburgers[i] = "E"
          print(f"{i}, {j}, {hamburgers[j]}")
          break
      finally:
        print()

print(hamburgers)
print(hamburgers.count("E"))

# 8 3
# PPHHHHPP

# 12 1
# HPHPHPHHPPHP

