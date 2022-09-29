
for tc in range(1,11):
    t = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]



    #시작점 잡아주기
    for j in range(100):
        if arr[99][j] == 2:
            row = 99
            col = j
    dy = [0, 0, -1]
    dx = [-1,1,0]
            
    #여기저기 찔러,,,
    while row > 0:
        for d in range(3):
            if 0 <= row+dy[d] <=99 and 0 <= col+dx[d] <=99:
                if arr[row+dy[d]][col+dx[d]] == 1:
                    arr[row][col] = 2
                    row = row + dy[d]
                    col = col + dx[d]
                    break
    print(f'{tc} {col}')

