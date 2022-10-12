T = int(input())
for testcase in range(1,T+1):
    K,N,M = map(int,input().split())
    bus = list(map(int,input().split()))
    present = 0
    cnt = 0
    next= present + K
    while next < N:
        if next in bus:
            present = next
            next += K
            cnt +=1
        else:
            next-=1
        if next == present:
            cnt = 0
            break
    print(f'#{testcase} {cnt}')
        




            
            