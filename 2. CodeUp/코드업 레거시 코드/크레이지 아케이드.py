# 8 1525 크레이지 아케이드
CrazyArcade = [[-1 for j in range(12)]for i in range(12)]

CrazyArcadeCpy = []

Player = []

#붙여넣기할 배열
for i in range(10):
    CrazyArcadeCpy.append(list(map(int,input().split())))

#배열 복사
for i in range(1,11):
    for j in range(1,11):
        CrazyArcade[i][j] = CrazyArcadeCpy[i-1][j-1]

#상하좌우 벽 판단 
toggle = [0 for i in range(4)]

#메인 
for i in range(1,11):
    for j in range(1,11):
        #물풍선 상하좌우 물줄기
        if CrazyArcade[i][j] >= 1:
            for T in range(1,CrazyArcade[i][j]+1):
                if (i+T <= 10) and (CrazyArcade[i+T][j] < 1):
                    if (CrazyArcade[i+T][j] != -1) and (toggle[0] == 0):
                        # print(f"하  + {T}")
                        CrazyArcade[i+T][j] = -2
                    else:
                        toggle[0] = 1
                if (CrazyArcade[i-T][j] < 1): 
                    if (CrazyArcade[i-T][j] != -1) and (toggle[1] == 0):
                        # print(f"상  + {T}")
                        CrazyArcade[i-T][j] = -2
                    else:
                        toggle[1] = 1
                        
                if(j + T <= 10) and (CrazyArcade[i][j+T] < 1):
                    if (CrazyArcade[i][j+T] != -1) and (toggle[2] == 0):
                        # print(f"우  + {T}")
                        CrazyArcade[i][j+T] = -2
                    else:
                        toggle[2] = 1
                if(CrazyArcade[i][j-T] < 1): 
                    if (CrazyArcade[i][j-T] != -1) and (toggle[3] == 0):
                        # print(f"좌  + {T}")
                        CrazyArcade[i][j-T] = -2
                    else:
                        toggle[3] = 1
            CrazyArcade[i][j] = -2
            toggle[0] = 0
            toggle[1] = 0
            toggle[2] = 0
            toggle[3] = 0

#플레이어 좌표 입력
n = int(input())
for i in range(n):
    Player.append(list(map(int,input().split())))
    if  CrazyArcade[Player[i][0]][Player[i][1]] == 0:
        CrazyArcade[Player[i][0]][Player[i][1]] = i + 1
        Player[i] = 1
    else:
        Player[i] = 0

#출력
for i in range(1,11):
    for j in range(1,11):
        print(CrazyArcade[i][j],end=" ")
    print("")

print("Character Information")
for i in range(n):
    if Player[i] == 1:
        print(f"player {i+1} survive")
    elif Player[i] == 0:
        print(f"player {i+1} dead")