
def isomok(y,x):
    dy  =[-1,1,0,0,-1,-1,1,1] #상하좌우대각선
    dx = [0,0,-1,1,-1,1,-1,1]
    for i in range(8):
        cnt = 1
        while 1:
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or nx > N-1 or ny > N-1:break
            if MAP[ny][nx] == '.':
                break
            if MAP[ny][nx] == 'o':
                cnt += 1
                y = ny
                x = nx
        if cnt >= 5:
            return True
    return False


T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    flag = 0
    MAP = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 'o':
                if isomok(i,j):
                    flag = 1
                    break
        if flag == 1:
            break
    
    if flag == 1:
        print(f'#{testcase} YES')
    else:
        print(f'#{testcase} NO')
'''
4
5
....o
...o.
..o..
.o...
o....
5
...o.
ooooo
...o.
...o.
.....
5
.o.oo
oo.oo
.oo..
.o...
.o...
5
.o.o.
o.o.o
.o.o.
o.o.o
.o.o.
'''