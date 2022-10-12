T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    arr = [[0] *N for _ in range(N)]
    y = 0
    x = 0
    cnt = 1
    idx = 0
    arr[0][0] = 1
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    while cnt < N * N:
        ny = y + dy[idx]
        nx = x + dx[idx]
        if 0<=ny <=N-1 and 0 <=nx <=N-1 and arr[ny][nx] == 0:
            cnt += 1
            arr[ny][nx] = cnt
            y = ny
            x = nx
            
        else:
            idx = (idx+1) % 4

    print(f'#{testcase}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j],end= ' ')
        print()
        

            
                
    



            
    
