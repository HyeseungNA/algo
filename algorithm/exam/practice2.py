#0은 안전지대, 1은 폭탄,3은 산을 가리킨다. 폭탄은 상하좌우로 퍼지면서 터지는데 산을 만나면 폭탄이 멈춘다.그렇다면 폭탄이 다 터진 후에 남은 안전지대는 총 몇 군일까?
#답은 4가 나와야함
def isbomb(y,x):
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    for m in range(4):
        index = 1
        while 1:
            ny = y + (dy[m] * index)
            nx = x + (dx[m] * index)
            if ny < 0 or nx < 0 or ny > 4 or nx > 4 or arr[ny][nx] == 3:
                break
            if arr[ny][nx] == 0:
                print(ny,nx)
                arr[ny][nx] = 2
            index += 1

arr = [[0,0,3,0,0],
       [0,3,1,0,3],
       [0,3,1,0,3],
       [3,0,0,1,0],
       [0,3,1,0,3]
        ]

for i in range(5):
    for j in range(5):
        if arr[i][j] == 1:
            isbomb(i,j)
cnt = 0
for i in range(5):
    for j in range(5):
        if arr[i][j] == 0:
            cnt += 1
print(cnt)            