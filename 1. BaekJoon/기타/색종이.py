n = int(input())
cnt = 0
arr = []
colorPaper = [[0 for _ in range(100)]for x in range(100)]

for i in range(n):
    arr.append(list(map(int,input().split())))

for k in range(n):
    x = arr[k][0]
    y = arr[k][1]
    for i in range(x,x+10):
        for j in range(y,y+10):
            colorPaper[i][j] = 1

for i in range(100):
    for j in range(100):
        if colorPaper[i][j] == 1:
            cnt +=1
print(cnt)