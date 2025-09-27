# 6 1515 생명 게임 1
# lifeGame = [[0] * 27 for j in range(27)]
# lifeGameCpy = []
# lifeCnt = 0

# for i in range(25):
#     lifeGameCpy.append(list(map(int,input().split())))

# for i in range(1,26):
#     for j in range(1,26):
#         lifeGame[i][j] = lifeGameCpy[i-1][j-1]


# for i in range(1,26):
#     for j in range(1,26):
#         lifeCnt = lifeGame[i-1][j-1]+lifeGame[i][j-1]+lifeGame[i+1][j-1]+lifeGame[i-1][j]+lifeGame[i+1][j]+lifeGame[i-1][j+1]+lifeGame[i][j+1]+lifeGame[i+1][j+1]
#         # print(lifeCnt)
#         if lifeGame[i][j] == 1:
#             if lifeCnt >= 4 or lifeCnt <= 1:
#                 # print('생명사망')
#                 # lifeGame[i][j] = 0
#                 lifeGameCpy[i-1][j-1] = 0
#                 #lifeCnt = 0

#         elif lifeGame[i][j] == 0:
#             if lifeCnt == 3:
#                 # print('생명탄생')
#                 # lifeGame[i][j] = 1
#                 lifeGameCpy[i-1][j-1] = 1
#                 #lifeCnt = 0
# # print('')
# for i in range(25):
#     for j in range(25):
#         print(lifeGameCpy[i][j],end=" ")
#     print("")



# 7 1520 생명 게임 2

a,b = map(int,input().split())

x,y,z = map(int,input().split())

lifeGameCpy = []
lifeGame = [[0 for i in range(b+2)] for j in range(a+2)]

for i in range(a):
    lifeGameCpy.append(list(map(int,input().split())))

k = int(input())

for i in range(1,a+1):
    for j in range(1,b+1):
        lifeGame[i][j] = lifeGameCpy[i-1][j-1]


for t in range(k):
    for i in range(1,a+1):
        for j in range(1,b+1):
            lifeCnt = lifeGame[i-1][j-1]+lifeGame[i][j-1]+lifeGame[i+1][j-1]+lifeGame[i-1][j]+lifeGame[i+1][j]+lifeGame[i-1][j+1]+lifeGame[i][j+1]+lifeGame[i+1][j+1]
            if lifeGame[i][j] == 1:
                if (lifeCnt >= z) or (lifeCnt < y):
                    # print('생명사망')
                    lifeGameCpy[i-1][j-1] = 0
                    
            elif lifeGame[i][j] == 0:
                if lifeCnt == x:
                    # print('생명탄생')
                    lifeGameCpy[i-1][j-1] = 1
    for w in range(1,a+1):
        for h in range(1,b+1):
            lifeGame[w][h] = lifeGameCpy[w-1][h-1]

#출력
for i in range(1,a+1):
    for j in range(1,b+1):
        print(lifeGame[i][j],end=" ")
    print("")