T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    index = 0
    st = (N//2)
    ed = (N//2)
    total = 0
    while index <= N-1:  # y축 인덱스가 N-1일때까지 반복
        for i in range(st,ed+1):
            total += arr[index][i]  
        if index < (N//2):  # y축 인덱스가 절반보다 작을때
            st -= 1  # 시작점 끝점 범위 늘려주기
            ed+= 1
        elif index >= (N//2):  # y 축 인덱스가 절반보다 클때
            st += 1  #시작점 끝점 범위를 다시 줄여주기
            ed-=1
        index += 1
    print(f'#{testcase} {total}')

