T = int(input())
for testcase in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(input()) for _ in range(N)]
    MIN = N * M
    w_cnt = 0
    
    r_cnt = 0
    for i in range(N-2):  
        for j in range(M):
            if arr[i][j] != 'W':
                w_cnt += 1
        b_cnt = 0
        for m in range(i+1,N-1): 
            for n in range(M):
                if arr[m][n] != 'B':
                    b_cnt += 1
            
            r_cnt = 0
            for k in range(m+1,N): 
                for l in range(M):
                    if arr[k][l] != 'R':
                        r_cnt += 1
            
            if MIN > w_cnt + b_cnt + r_cnt:
                MIN = w_cnt + b_cnt + r_cnt
    print(f'#{testcase} {MIN}')

'''
2
4 5
WRWRW
BWRWB
WRWRW
RWBWR
'''