def dfs(y,x):
    global flag
    if y == 3 and x == 3:
        flag = 1
        return 
    directy = [-1,1,0,0]
    directx = [0,0,-1,1]
    for i in range(4):
        dy = y + directy[i]
        dx = x + directx[i]
        if dy < 0 or dx < 0 or dy > 3 or dx > 3:
            continue
        if arr[dy][dx] == 1:
            continue
        if visited[dy][dx] == 1:continue
        visited[dy][dx] = 1
        dfs(dy,dx)

flag = 0
arr= [
    [0,0,0,0],
    [1,0,1,0],
    [1,0,1,0],
    [0,0,0,0]
]

visited = [[0]*4 for _ in range(4)]
visited[0][0] = 1
dfs(0,0)
if flag == 1:
    print('찾을 수 있음')
else:
    print('찾을 수 없음')