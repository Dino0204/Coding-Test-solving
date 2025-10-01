# 1. 1차원 배열 선언
maze = []

# 한줄 마다 1차원 배열을 입력받고 이 배열을 maze 배열의 인수로 포함시킴
for i in range(10):
    maze.append(list(map(int,input().split())))

# 2. []를 첫번째 인수로 갖는 2차원 배열 선언
maze2 = [[]]

# 3. [0]를 0 ~ 9 인수로 갖는 2차원 배열 선언
maze3 = [[0]for _ in range(10)]
