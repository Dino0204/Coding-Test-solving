# def n_queens(i,col): #
#     n=len(col)-1
#     if (promising(col,i)):
#         if(i==n):
#             print(col[1:n+1])
#         else:
#             for j in range(1,n+1):
#                 col[i+1] = j
#                 n_queens(col,i+1)

# def promising(i,col):   
#     k=1
#     flag = True
#     while (k < i and flag): #
#         if(col[i] == col[k] or abs(col[i] - col[k]) == (i-k)):
#             flag = False
#             k+=1
#     return flag

# def main():
#     n = int(input())
    

# if __name__ == '__main__':
#     main()
    
#col : 열 / row : 행

# def nqueens(i, col):
#     n = len(col) - 1 # n = main(n)
#     if (promising(col, i)): # True or False
#         if(i == n): # 1차원 배열을 다 끝냈다면 종료
#             print(col[1:n+1]) # 1 ~ n까지의 행
#         else:
#             for j in range(1, n+1): # 1 ~ n까지
#                 col[i+1] = j # 다음행에 j를 넣음
#                 nqueens(i+1, col) # 재귀

# def promising(i, col):# col , i
#     k = 1 
#     flag = True
#     while (k < i and flag): 
#         if(col[i] == col[k] or (abs(col[i] - col[k]) == (i - k))): # 행 값이 같거나 행 값끼리 뺀 절댓값이 행 좌표와 같다면 재귀종료
#             flag = False 
#         k += 1
#     return flag

# def main():
#     n = int(input())
#     col = [0] * (n+1) # 1차원 배열 0 | 1 2 3 4 5 6 7 8 
#     nqueens(0, col)

# 전치행렬
print("행 수를 입력하시오: ",end=" ")
m = int(input())
print("열 수를 입력하시오: ",end=" ")
n = int(input())
arr = [[0 for i in range(n)] for j in range(m)]
TmArr = [[0 for i in range(m)] for j in range(n)]

for i in range(m):
    for j in range(n):
        print(f"{i+1}행 {j+1}열의 원소를 입력하시오: ",end=" ")
        arr[i][j] = int(input())
        TmArr[j][i] = arr[i][j]

print('입력 한 행렬')
for i in range(m):
    for j in range(n):
        print(arr[i][j],end=" ")
    print('')

print('전치행렬')
for j in range(n):
    for i in range(m):
        print(TmArr[j][i],end=" ")
    print('')


# n = int(input())
# sum = n

# for i in range(n-1,0,-1):
#     sum*=i
# print(sum)



# def gibu(k):
#     sum = 0
#     if(k%2==0):
#         for i in range(0,k,+2):
#             sum+=10
#     else:
#         for i in range(0,k,+2):
#             sum+=1
#     return sum
# k,h = map(int,input().split())
# print(gibu(k) + gibu(h)) 

# n = int(input())
# max = min = n
# for i in range(1,5):
#     n = int(input())
#     if(max < n):
#         max = n
#     if(min > n):
#         min = n
# print(max)
# print(min)

# k = int(input())
# for i in range(1,7):
#     if i < k and (k-i>=1 and k-i <=6):
#         print(i,k-i)

# for i in range(1,10):
#     for j in range(2,6):
#         print(f"{j} x {i} = {i*j}",end="   ")
#     print('')

# n = int(input())

# arr = list(map(int, input().split()))

# for i in range(n-1,-1,-1):
#     print(arr[i],end=" ")







# k = int(input())

# arr = list(map(int,input().split()))

# for i in range(2):
#     for j in range(k):
#         print(arr[j])

# n = int(input())
# arr = list(map(int,input().split()))
# for i in range(n):
#     print(f'{i+1}',end=": ")
#     for j in range(n):
#         if i!=j:
#             if arr[i] < arr[j]:
#                 print('<',end=" ")
#             elif arr[i] > arr[j]:
#                 print('>',end=" ")
#             else:
#                 print('=',end=" ")
#     print('')








# n,c = map(int,input().split())
# arr = list(map(int,input().split()))
# print(arr)

# for i in range(n):
#     for j in range(n,i,-1):
        

    
    # 5 3 4 1 2
    # 5 3 4 1 2
    # 5 3 1 4 2
    # 5 1 3 4 2
    # 1 5 3 4 2
    
    # 1 5 3 2 4
    # 1 5 2 3 4
    # 1 2 5 3 4
    
    # 1 2 5 3 4
    # 1 2 3 5 4
    
    # 1 2 3 4 5

