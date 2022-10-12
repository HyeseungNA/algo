for testcase in range(1,11):
    tc = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                row = i
                col = j
    
    while row > 0:
        dy = [0,0,-1]
        dx = [-1,1,0]
        idx = 0
        while 1:
            nr = row + dy[idx]
            nc = col + dx[idx]
            # 찾으면 다시 좌우상
            if 0<= nr <= 99 and 0<= nc <= 99 and arr[nr][nc] == 1:
                arr[nr][nc] = 3
                row = nr
                col = nc
                break
            # 못 찾으면 계속해서 찾기
            else:
                idx = (idx+1) % 4
    print(f'#{testcase} {col}')



