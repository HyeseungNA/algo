def cover(y,x,k):
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    for m in range(4):
        for n in range(1,k+1):
            ny = y + (dy[m] * n)
            nx = x + (dx[m] * n)
            if nx < 0 or ny < 0 or nx > N-1 or nx > N-1:continue
            if arr[ny][nx] == 'H':
                arr[ny][nx] = 'X'

T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    dict1 = {'A':1,'B':2,'C':3}
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 'H' and arr[i][j] != 'X':
                k = dict1[arr[i][j]]
                cover(i,j,k)
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
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