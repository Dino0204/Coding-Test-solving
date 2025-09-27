# 1 1507 4개의 직사각형 넓이

# nemo = [[0 for _ in range(100)]for x in range(100)]
# arr = []
# cnt = 0

# #(1,2) , (3,4) / (2,3) , (5,7) ...
# # arr[0][0] == 1 , arr[0][1] = 2 ...

# for i in range(4):
#     arr.append(list(map(int,input().split())))

# for i in range(4):
#     for j in range(arr[i][0],arr[i][2]):
#         for k in range(arr[i][1],arr[i][3]):
#             nemo[j][k] = 1

# for i in range(100):
#     for j in range(100):
#         if nemo[i][j] == 1:
#             cnt+=1

# print(cnt)



# 2 1508 나도 IQ 150

# n = int(input())
# tri = [[0 for _ in range(n)]for x in range(n)]

# for i in range(n):
#     tri[i][0] = int(input())

# for i in range(n):
#     for j in range(n):
#         if i+1 >= n or j+1 >= n:
#             break
#         tri[i+1][j+1] = tri[i+1][j] - tri[i][j]


# for i in range(n):
#     for j in range(i+1):
#         if tri[i][j] != 0:
#             print(tri[i][j],end=" ")
#     print("")


# 3 1509 진격 후 결과
# k > 0 : 블럭 장애물 / k == 0 : 평지 / k < 0 : 구덩이 장애물

# board = []

# for i in range(10):
#     board.append(list(map(int,input().split())))

# mal = list(map(int,input().split()))


# for i in range(10):
#     if(mal[i]==1):
#         for j in range(9,-1,-1):
#             if(board[j][i] > 0):
#                 print(f"{i+1} crash")
#                 break
#             elif(board[j][i] < 0):
#                 print(f"{i+1} fall")
#                 break
#             elif j == 0:
#                 print(f"{i+1} safe")



# 3 1510 홀수 마방진
# n = int(input())

# magicSqure = [[0 for x in range(n)]for y in range(n)]

# i = 0
# j = n//2
# test = 1

# # While문으로 변경
# # for i in range(n,-1,-1):
# #     for j in range(h,n):
# #         magicSqure[i][j] = num
# #         num+=1

# while(test <= n*n):
#     magicSqure[i][j] = test
#     if test%n !=0:
#         j+=1
#         i-=1    
#     else:
#         i+=1

#     if i < 0:
#         i = n-1
#     if j > n-1:
#         j = 0

#     test+=1

# for k in range(n):
#     for l in range(n):
#         print(magicSqure[k][l],end=" ")
#     print("")



# 4 1511 테두리의 합
# n = int(input())

# arr = [[0 for x in range(n)]for y in range(n)]
# num = 1
# result = 0

# for i in range(n):
#     for j in range(n):
#         arr[i][j] = num
#         if j == 0 or j == n-1:
#             result += num
#         elif i == 0 or i == n-1:
#             result += num
#         num += 1

# # 인덱스 0 idx / n - 1 idx
# # 출력
# # for i in range(n):
# #     for j in range(n):
# #         print(arr[i][j],end=" ")
# #     print("")

# print(result)



# 5 1512 숫자 등고선
# n = int(input())
# x,y = map(int,input().split())

# x -= 1
# y -= 1

# contourLine = [[0 for i in range(n)]for j in range(n)]

# num = 1
# contourLine[x][y] = num


# # ???? ??? ?? ? ?? ??? ????
# for i in range(n):
#     for j in range(n):


# for i in range(n):
#     for j in range(n):
#         print(contourLine[i][j],end=" ")
#     print("")

# # print(n,x,y)
# # i + - 1 / j + - 1 / 
# # 만약 숫자가 0 이라면 채웠던 숫자 동서남북으로 채움

# 2차원 배열 빗금 1

# n,m = map(int,input().split())
# arr = [[0 for i in range(m)]for j in range(n)]

# x = 0
# idx = 1

# for k in range(n*m):
#   for i in range(m):
#     for j in range(n):
#       if i + j == k:
#         arr[j][i] = idx
#         idx += 1
#         # for l in range(n):
#         #   for h in range(m):
#         #     print(arr[l][h],end=" ")
#         #   print("")
#         # print("")


# for i in range(n):
#   for j in range(m):
#     print(arr[i][j],end=" ")
#   print("")



# 2차원 배열 빗금 2

# n,m = map(int,input().split())
# arr = [[0 for i in range(m)]for j in range(n)]

# x = 0
# idx = 1

# for k in range(n*m):
#   for i in range(n):
#     for j in range(m):
#       if i + j == k:
#         arr[i][j] = idx
#         idx += 1
#         # for l in range(n):
#         #   for h in range(m):
#         #     print(arr[l][h],end=" ")
#         #   print("")
#         # print("")


# for i in range(n):
#   for j in range(m):
#     print(arr[i][j],end=" ")
#   print("")



# # 2차원 배열 빗금 3

# n,m = map(int,input().split())
# arr = [[0 for i in range(m)]for j in range(n)]

# x = 0
# idx = 1

# for k in range(n*m):
#   for i in range(n):
#     for j in range(m-1,-1,-1):
#       if i + j == k:
#         arr[i][j] = idx
#         idx += 1
#         # for l in range(n):
#         #   for h in range(m):
#         #     print(arr[l][h],end=" ")
#         #   print("")
#         # print("")


# for i in range(n):
#   for j in range(m-1,-1,-1):
#     print(arr[i][j],end=" ")
#   print("")













