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