def isbaduk(y,x,color):
    dy = [-1,1,0,0,-1,-1,1,1]
    dx = [0,0,-1,1,-1,1,-1,1]
   
    if color == 1:  #흑돌이면
        for i in range(8):
            lst = []
            s_y = y
            s_x = x
            while 1:
                ny = s_y + dy[i]
                nx = s_x + dx[i]
                if nx < 0 or ny < 0 or nx > N-1 or ny > N-1: #범위를 벗어나면 리스트 초기화
                    lst = []
                    break
                if baduk[ny][nx] == 0: # 아무것도 없어도 초기화
                    lst = []
                    break
                if baduk[ny][nx] == 2: #다른색이면 리스트안에 넣기
                    lst.append([ny,nx])
                    s_y = ny
                    s_x = nx
                if baduk[ny][nx] == 1:  # 같은 색을 만나면 이동 멈추기
                    for r,c in lst:
                        baduk[r][c] = 1
                    break
                    
    elif color == 2:  #흑돌이면
        for i in range(8):
            lst = []
            s_y = y
            s_x = x
            while 1:
                ny = s_y + dy[i]
                nx = s_x + dx[i]
                if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:
                    lst = []
                    break
                if baduk[ny][nx] == 0:
                    lst = []
                    break
                if baduk[ny][nx] == 1:
                    lst.append([ny,nx])
                    s_y = ny
                    s_x = nx
                if baduk[ny][nx] == 2:
                    for rr,cc in lst:
                        baduk[rr][cc] = 2
                    break

T = int(input())
for testcase in range(1,T+1):
    N,M = map(int,input().split())
    baduk = [[0]*N for _ in range(N)]
    baduk[(N-1)//2][(N-1)//2] = 2
    baduk[(N-1)//2+1][(N-1)//2+1] =2
    baduk[(N-1)//2][(N-1)//2+1] = 1
    baduk[(N-1)//2+1][(N-1)//2] = 1
    for _ in range(M):
        x,y,color = map(int,input().split())
        baduk[y-1][x-1] = color
        isbaduk(y-1,x-1,color)
    black = 0
    white = 0
    for m in range(N):
        for n in range(N):
            if baduk[m][n] ==2 :
                black += 1
            elif baduk[m][n] ==1:
                white += 1
    print(f'#{testcase} {white} {black}')
            


'''
1
4 12
1 2 1
1 1 2
4 3 1
4 4 2
2 1 1
4 2 2
3 4 1
1 3 2
2 4 1
1 4 2
4 1 2
3 1 2
'''

for testcase in range(1,11):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N-1):
            for jj in range(j+1,N):
                if arr[j][i] == 2:  # 빨간색 자성체를 기준으로 
                    if arr[jj][i] ==1: # 그 밑에 푸른 자성체가 있으면
                        cnt+=1    # 교착점을 카운트 해주고
                        arr[jj][i] = 3  # 푸른 자성체를 다른 색으로 만들기
                        break
                    elif arr[jj][i] == 3: #다른 색 자성체를 만나면 밑으로 탐색할 수 없으니 브레이크
                        break
                        
    print(f'#{testcase} {cnt}')


'''

5
2 0 0 0 2
2 0 0 2 1
1 2 0 1 2
2 0 0 1 1
1 1 2 1 1
    '''


def ispattern(y, x, c):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    for d in range(4):
        if c == '.':
            ny = y + dy[d]
            nx = x + dx[d]
            if nx < 0 or ny < 0 or nx > M - 1 or ny > N - 1:
                continue
            if arr[ny][nx] == '.':
                return False
            if arr[ny][nx] == '?':
                arr[ny][nx] = '#'
        elif c == '#':
            ny = y + dy[d]
            nx = x + dx[d]
            if nx < 0 or ny < 0 or nx > M - 1 or ny > N - 1:
                continue
            if arr[ny][nx] == '#':
                return False
            if arr[ny][nx] == '?':
                arr[ny][nx] = '.'
    return True


T = int(input())
for testcase in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(M):
            if not ispattern(i, j, arr[i][j]):
                flag = 1
                break
        if flag == 1:
            print(f'#{testcase} impossible')
            break
    else:
        print(f'#{testcase} possible')
'''
3
3 6
#.????
?#????
???.??
1 6
##????
3 3
.#.
#?#
.#.
'''


for tc in range(1, 1 + int(input())):
    x, y = map(int, input().split())

    mapp = []
    for i in range(x):
        mapp.append(list(input()))

    B = []
    W = []

    for i in range(x):
        for j in range(y):
            if mapp[i][j] == '#':  # '#'이면 B에 x+y를 2로 나눈 나머지 (0 또는 1)
                B.append((i + j) % 2)
            elif mapp[i][j] == '.':  # '.'이면 W에 x+y를 2로 나눈 나머지 (0 또는 1)
                W.append((i + j) % 2)

    B_L, W_L = len(set(B)), len(set(W))

    if B_L > 1 or W_L > 1:  # 두 종류 이상의 값이 들어있을 때
        print(f'#{tc} impossible')

    elif B_L == 1 and W_L == 1:  # 각각 하나의 종류의 값이 들어있을 때
        if set(B) == set(W):  # 그 값이 서로 같을 때
            print(f'#{tc} impossible')
        else:  # 그 값이 서로 다를 때
            print(f'#{tc} possible')
    else:  # 둘 중 하나 이상이 비었을 때
        print(f'#{tc} possible')