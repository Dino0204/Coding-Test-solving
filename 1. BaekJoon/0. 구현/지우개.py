n = int(input())

arr = list(i for i in range(1, n+1))

while len(arr) > 1:
  arr = list(filter(lambda x: arr.index(x) % 2 != 0, arr))

print(arr[0])