
T = int(input())
for testcase in range(1,T+1):
    N, Q = map(int,input().split())
    for _ in range(Q):
        L,R = map(int,input().split())
    bucket = [0] * (N+1)
    for i in range(Q):
        for j in range(L,R+1):
            bucket[j] = i
    print(f'#{testcase}',end = ' ')
    for m in range(1,N+1):
        print(bucket[m],end = ' ')
    print()
