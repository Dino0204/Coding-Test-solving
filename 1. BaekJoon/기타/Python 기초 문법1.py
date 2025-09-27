# 1. Sep
# y, m ,d = input().split('.')
# print(d,m,y,sep='-')

# 2. int()
# n = int(input())
# if n%7==0:
#     print('multiple')
# else:
#     print('not multiple')

# len = int(input())

# 3. And,Or
# if ((len >= 50) and (len <= 70))or(len%6==0):
#     print('win')
# else:
#     print('lose')

# 4. day
# day = int(input())
# if (day==2)or(day==4)or(day==6):
#     print('enjoy')
# else:
#     print('oh my god')

# 5. Saju
# map(func name, values)
# y,m,d=map(int,input().split())
# if ((y+m+d)//100)%2==0:
#     print('대박')
# else:
#     print('그럭저럭')

# 6. BMI
# BMI = int(input())
# if BMI <=10:
#     print('정상')
# elif BMI <=20:
#     print('과체중')
# elif BMI > 20:
#     print('비만')

# 7. operator
# a,b = map(int,input().split())
# arr = [a+b,a-b,a*b,a/b,a**b,b+a,b-a,b*a,b/a,b**a]
# print(float(max(arr)))

# 8. For
# n = int(input())
# sum = 0
# for n in range(1,n+1):
#     if(n%2==0):
#         sum += n
# print(n)
# print(sum)

# 9. prime
# n = int(input())
# for i in range(2,n):
#     if(n%i==0):
#         print('not prime')
#         quit()
# print('prime')

# 10. factorial
# n = int(input())
# sum = 1
# for i in range(n,1,-1):
#     sum*=i
# print(sum)

# 11.
# a,b = map(int,(input().split()))
# sum = 0
# for i in range(a,b+1):
#     if i%2==0:
#         sum-=i
#         print('-',end='')
#     else:
#         sum+=i
#         if i!= a:
#             print('+',end='')
#     print(i,end='')
# #print('=',sum,sep='')
# print(f'={sum}')
# #print('-',a,'=',sum,sep='')
# #print(f"-{a}={sum}")

# 12.
# cnt = 1
# n = int(input())
# while n>=10:
#     cnt+=1
#     n /= 10
# print(cnt)

# 13.
# 34 - 9 => n-k
# 25 / 36 => 5 / 6 => t**t
# n = int(input())
# t = 1
# while t*t < n :
#     t+=1
# t-=1
# print(n-t*t,t)

# 14.
# n = int(input())
# for i in range(0,n):
#     for j in range(0,i):
#         print(' ',end='')
#     for j in range(n,i,-1):
#         print('*',end='')
#     print('')

# n = int(input())
# for i in range(0,n):
#     print(' '*i,end='')
#     print('*'*(n-i),end='')
#     print('')

# 15.
# n,k = map(int,input().split())
# for i in range(n):
#     for j in range(n):
#         if ((i==0)or(i==n-1)or(j==0)or(j==n-1))or((i+j+1)%k==0):
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print('')

# 16.
# n = int(input())
# l=list(map(int,input().split()))
# result = [0]*24
# for i in range(n):
#     result[l[i]]+=1
# for i in range(1,24):
#     print(result[i],end=' ')

# 17.
# n = int(input()) 

# arr = [[0 for i in range(n)]for j in range(n)]
# k = 1

# for i in range(n):
#     for j in range(n):
#         arr[i][j] = k
#         k+=1
        
# for i in range(n):
#     for j in range(n):
#         print(arr[i][j],end=" ")
#     print("")

# 18.
# n = int(input()) 

# arr = [[0 for i in range(n)]for j in range(n)]
# k = 1

# for i in range(n):
#     for j in range(n-1,-1,-1):
#         arr[i][j] = k
#         k+=1


# for i in range(n):
#     for j in range(n):
#         print(arr[i][j],end=" ")
#     print("")

# 19.

# n = int(input())

# baduk = [[0 for i in range(20)]for j in range(20)]

# for i in range(n):
#     x,y = map(int,input().split())
#     baduk[x][y] = 1

# for i in range(1,20):
#     for j in range(1,20):
#         print(baduk[i][j],end=" ")
#     print("")

# 20.

# baduk = []

# for i in range(19):
#     baduk.append(list(map(int, input().split())))

# n = int(input())

# for i in range(n):
#     x,y = map(int,input().split())
#     for j in range(19):
#         if baduk[x-1][j] == 1:
#             baduk[x-1][j] = 0
#         else:
#             baduk[x-1][j] = 1
            
#         if baduk[j][y-1] == 1:
#             baduk[j][y-1] = 0
#         else:
#             baduk[j][y-1] = 1

# for i in range(19):
#     for j in range(19):
#         print(baduk[i][j],end=" ")
#     print("")

# 21.

# h,w = map(int,input().split())
# arr = [[0 for i in range(w)]for j in range(h)]
# n = int(input())

# for i in range(n):
#     l,d,x,y = map(int,input().split())
#     # 가로
#     if d == 0:
#         for j in range(l):
#             arr[x-1][y-1+j] = 1
#     # 세로
#     else :
#         for j in range(l):
#             arr[x-1+j][y-1] = 1



# for i in range(h):
#     for j in range(w):
#         print(arr[i][j],end=" ")
#     print("")

# 22.

# 개미굴에서 먹이까지의 가장 빠른 길
# 출발지 : 2 , 2 | 오른쪽, 아래로만 갈 수 있음 | 테두리는 전부 벽
# 0 갈 수 있는 곳 | 1 못 가는 곳 | 2 먹이지점

# maze = []
# for i in range(10):
#     maze.append(list(map(int, input().split())))

# k = 1
# h = 1
# Test = 0 

# while Test < 100:
#     Test+=1
#     # print(Test) 
#     if maze[k][h]==0:
#         maze[k][h]=9
#     elif maze[k][h]==2:
#         # print("종료1")
#         maze[k][h]=9
#         break
    
#     elif (maze[k+1][h] == 1 and maze[k][h+1] == 1) or (k >= 8 and h >= 8):
#         # print("종료2")
#         break
    
#     if maze[k][h+1] != 1:
#         h+=1
#     elif maze[k+1][h] != 1:
#         k+=1


# for i in range(10):
#     for j in range(10):
#         print(maze[i][j],end=" ")
#     print("")

# 23.

# x = 1
# n = int(input())
# Arr = [[0 for i in range(n)]for j in range(n)]

# for i in range(n):
#     for j in range(n):
#         Arr[i][j] = x
#         x+=1

# for i in range(n):
#     for j in range(n):
#         print(Arr[i][j],end=" ")
#     print("")

# 24.

# x = 1
# n = int(input())
# Arr = [[0 for i in range(n)]for j in range(n)]

# for i in range(n):
#     for j in range(n):
#         Arr[j][i] = x
#         x+=1

# for i in range(n):
#     for j in range(n):
#         print(Arr[i][j],end=" ")
#     print("")

# 25.

# x = 1
# n = int(input())
# Arr = [[0 for i in range(n)]for j in range(n)]

# for i in range(n):
#     for j in range(n-1,-1,-1):
#         Arr[j][i] = x
#         x+=1

# for i in range(n):
#     for j in range(n):
#         print(Arr[i][j],end=" ")
#     print("")

# 26.

# n,m = map(int,(input().split()))
# x = n*m
# Arr = [[0 for i in range(m)]for j in range(n)]

# for i in range(n):
#     for j in range(m):
#         Arr[i][j] = x
#         x-=1

# for i in range(n):
#     for j in range(m):
#         print(Arr[i][j],end=" ")
#     print("")

# 27.
# n,m = map(int,(input().split()))
# A = [list(map(int,input().split()))for j in range(n)]
# B = [list(map(int,input().split()))for j in range(n)]

# for i in range(n):
#     for j in range(m):
#         print(f"{A[i][j]+B[i][j]}",end=" ")
#     print("")

# 28.
# Arr = [list(map(int,input().split()))for j in range(9)]
# Arr_max = Arr[0][0]
# x = 1
# y = 1

# for i in range(9):
#     for j in range(9):
#         if Arr_max <= Arr[i][j]:
#             Arr_max = Arr[i][j]
#             x = i + 1
#             y = j + 1

# print(Arr_max)
# print(x,y)









