def fiboRecursion(n):
  cnt = 0
  cnt += 1
  
  if n == 1 or n == 2:
    return cnt
  else:
    return fiboRecursion(n-1) + fiboRecursion(n-2)

def fiboNacci(n):
  cnt = 0
  fibo = [0 for _ in range(n)]
  
  fibo[0] = fibo[1] = 1
  for i in range(2,n):
    cnt += 1
    fibo[i] = fibo[i-1] + fibo[i-2]
  return cnt

n = int(input())

print(f"{fiboRecursion(n)} {fiboNacci(n)}")