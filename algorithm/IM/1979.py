T = int(input())
for testcase in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    #가로탐색
    total = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt +=1
            if j == N-1 or arr[i][j] == 0:
                if cnt == M:
                    total +=1
                cnt = 0
    #세로 탐색
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
            if j == N-1 or arr[j][i] == 0:
                if cnt == M:
                    total +=1
                cnt = 0
    print(f'#{testcase} {total}')


'''
10
5 3
0 0 1 1 1
1 1 1 1 0
0 0 1 0 0
0 1 1 1 1
1 1 1 0 1
'''