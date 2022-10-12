def gs(y,x):
    total = arr[y][x]
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    for k in range(1,M):
        for d in range(4):
            ny = y + dy[d] * k
            nx = x + dx[d] * k
            if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:continue
            total += arr[ny][nx]
    return total

def zz(y,x):
    total2 = arr[y][x]
    dy = [-1,-1,1,1]
    dx = [-1,1,-1,1]
    for kk in range(1,M):
        for dd in range(4):
            ny = y + dy[dd] * kk
            nx = x + dx[dd] * kk
            if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:continue
            total2 +=  arr[ny][nx]
    return total2


T = int(input())
for testcase in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    MAX = -21e8
    for i in range(N):
        for j in range(N):
            ret1= gs(i,j)
            ret2 = zz(i,j)
            if MAX < max(ret1,ret2):
                MAX = max(ret1,ret2)
    print(f'#{testcase} {MAX}')
'''
2
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
'''