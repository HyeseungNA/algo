T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    
    lst = []
    for i in range(N-1):
        cnt = 0
        for j in range(i+1,N):
            if arr[i] > arr[j]:
                cnt +=1
        lst.append(cnt)
    

    print(f'#{testcase} {max(lst)}')

