for testcase in range(1,11):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N-1):
            for jj in range(j+1,N):
                if arr[j][i] == 2:
                    if arr[jj][i] ==1:
                        cnt+=1 
                        arr[jj][i] = 3
                        break
                    elif arr[jj][i] == 3:
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

