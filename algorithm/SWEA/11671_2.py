def find(y,x,m):
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    for k in range(1,m+1):
        for d in range(4):
            ny = y + (dy[d] * k)
            nx = x + (dx[d] * k)
            if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:continue
            if MAP[ny][nx] == 'H':
                MAP[ny][nx] = 'X'
T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    MAP = [list(input()) for _ in range(N)]
    dic = {'A':1,'B':2,'C':3}
    for i in range(N):
        for j in range(N):
            if MAP[i][j] != 'H' and MAP[i][j] != 'X':
                m = dic[MAP[i][j]]
                find(i,j,m)
    cnt = 0
    for i in range(N):
        for j in range(N):
            if MAP[i][j] =='H':
                cnt += 1
    print(cnt)

'''
1
9
XXXXXXXXX
XXXHXXXXX
XXHAHXXHX
XXHHXXXXX
XXXXXXXXX
XXAHHXXXX
XXHXXHAHX
XXAHXXHXX
XXHXHXXXX

'''