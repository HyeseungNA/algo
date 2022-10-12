T = int(input())
for testcase in range(1,T+1):
    N,M = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    lst = []
    if N > M:
        for i in range(N-M+1):
            total = 0
            for j in range(M):
                total += a[i+j] * b[j]
            lst.append(total)
    if N < M:
        for i in range(M-N+1):
            total = 0
            for j in range(N):
                total += b[i+j] * a[j]
            lst.append(total)
    print(f'#{testcase} {max(lst)}')
'''
10
3 5
1 5 3
3 6 -7 5 4
'''