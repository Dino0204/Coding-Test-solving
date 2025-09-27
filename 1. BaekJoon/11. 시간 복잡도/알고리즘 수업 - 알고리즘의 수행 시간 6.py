# MenOfPassion
# sum = 0
# for i in range(1,n-1):
#   for j in range(i+1,n):
#     for k in range(j+1,n+1):
#       sum += A[i] * A[j] * A[k]
# return sum

# 시간복잡도 O((n-2) * (n - 1) * (n) // 3 // 2)
n = int(input())  
print((n-2) * (n - 1) * (n) // 3 // 2)
print(3)