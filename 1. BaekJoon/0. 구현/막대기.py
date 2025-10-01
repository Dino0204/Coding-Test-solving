import sys
input = sys.stdin.readline

n = int(input())

arr = [0]*n

for i in range(n):
  arr[i] = int(input())

max_stick = arr[n-1]
cnt = 1

for i in range(n-1,-1,-1):
  if(max_stick < arr[i]):
    # print(f"{max_stick} < {arr[i]}")
    max_stick = arr[i]
    cnt+=1

print(cnt)