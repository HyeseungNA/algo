def iskill(yy,xx):
    total = 0
    global MAX
    for y in range(M):
        for x in range(M):
            total += MAP[y+yy][x+xx]
        if MAX < total:
            MAX = total
    return 
    

T = int(input())
for testcase in range(1,T+1):
    N,M = map(int,input().split())
    MAP =[list(map(int,input().split())) for _ in range(N)]
    MAX = -21e8
    for i in range(N-M+1):
        for j in range(N-M+1):
            iskill(i,j)
    print(f'#{testcase} {MAX}')

'''
10
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3

'''