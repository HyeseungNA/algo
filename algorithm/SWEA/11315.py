#'O'인 지점 인덱스만 불러오기
# 벽에 닿거나 'O'가 아니면 끝내기
def omok(y,x):
    dy = [-1,1,0,0,-1,-1,1,1]
    dx = [0,0,-1,1,-1,1,-1,1]
    for i in range(8):
        cnt = 1
        while 1:
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:
                break
            if arr[ny][nx] == '.':
                break
            if arr[ny][nx] == 'o':
                cnt += 1
        if cnt >= 5:
            return True
    return False


T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] =='o':
                if omok(i,j):
                    print(f'{testcase} YES')
                    break
    print(f'{testcase} NO')
    


'''
1
5
....o
...o.
..o..
.o...
o....
'''
'''
4
5
.o.o.
o.o.o
.o.o.
o.o.o
.o.o.
'''