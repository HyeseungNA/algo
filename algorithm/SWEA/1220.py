for testcase in range(1,11):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N-1):
            for jj in range(j+1,N):
                if arr[j][i] == 2:  # 빨간색 자성체를 기준으로 
                    if arr[jj][i] ==1: # 그 밑에 푸른 자성체가 있으면
                        cnt+=1    # 교착점을 카운트 해주고
                        arr[jj][i] = 3  # 푸른 자성체를 다른 색으로 만들기
                        break
                    elif arr[jj][i] == 3: #다른 색 자성체를 만나면 밑으로 탐색할 수 없으니 브레이크
                        break
                        
    print(f'#{testcase} {cnt}')


'''

5
2 0 0 0 2
2 0 0 2 1
1 2 0 1 2
2 0 0 1 1
1 1 2 1 1
    '''

