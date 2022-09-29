T = int(input())
for testcase in range(1,T+1):
    N,Q = map(int,input().split())
    bucket = [0]*(N+1)
    for i in range(1,Q+1):
        L,R = map(int,input().split())
        for j in range(L,R+1):
            bucket[j] = i
    print(f'#{testcase}',end = ' ')
    for m in range(1,N+1):
        print(bucket[m],end = ' ')
    print()T = int(input())
for testcase in range(1,T+1):
    N,Q = map(int,input().split())
    bucket = [0]*(N+1)
    for i in range(1,Q+1):
        L,R = map(int,input().split())
        for j in range(L,R+1):
            bucket[j] = i
    print(f'#{testcase}',end = ' ')
    for m in range(1,N+1):
        print(bucket[m],end = ' ')
    print()
        
'''
1
5 2
1 3
2 4
'''        