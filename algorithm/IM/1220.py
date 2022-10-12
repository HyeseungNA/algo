for testcase in range(1,11):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        state = 0
        for j in range(N):
            if arr[j][i] == 1:
                state = 1
            elif arr[j][i] == 2 and state ==1:
                state = 0
                ans += 1
    print(f'#{testcase} {ans}')