
for testcase in range(1,11):
    n = int(input())
    arr = list(map(int,input().split()))
    for _ in range(n):
        arr.sort(reverse=True)
        arr[0]-=1
        arr[-1] +=1
    print(f'#{testcase} {max(arr)-min(arr)}')