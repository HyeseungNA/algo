T = int(input())
for testcase in range(1,T+1):
    N =int(input())
    bucket = [0]*5001
    for _ in range(N):
        a,b = map(int,input().split())
        for i in range(a,b+1):
            bucket[i] += 1
    P = int(input())
    print(f'#{testcase}',end = ' ')
    for _ in range(P):
        c = int(input())
        print(bucket[c],end = ' ')
    print()

'''
1
2
1 3
2 5
5
1
2
3
4
5
'''   