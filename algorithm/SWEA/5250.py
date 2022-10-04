def minimum():
    inf = int(21e8)
    cost = [[inf]*N for _ in range(N)]
    q = []
    q.append((0,0))
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    cost[0][0] = 0  #시작지 비용을 0으로 만들어주기
    while q:
        p = q.pop(0)  #큐가 빌 때까지
        for i in range(4): # 사방탐색
            ny = p[0] + dy[i]   
            nx = p[1] + dx[i]
            if 0 > ny or ny > N-1 or nx <0 or nx >N-1:continue 
            if 0 <= ny <= N-1 and 0 <= nx <= N-1:
                diff = 0  # 범위까지는 차이를 0으로
            
                if MAP[ny][nx] > MAP[p[0]][p[1]]:  #더 높으면 높이 차이
                    diff = MAP[ny][nx] - MAP[p[0]][p[1]]
                if cost[ny][nx] > cost[p[0]][p[1]] + diff + 1:
                    cost[ny][nx] = cost[p[0]][p[1]] + diff + 1
                    q.append((ny,nx))
    return cost[N-1][N-1]  #도착한 곳의 비용
    
                
T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    MAP = [list(map(int,input().split()))for _ in range(N)]
    #큐가 빌 때까지 반복하면서 최소값 찾기
    #처음은 다 가중치 1로 고정
    #이동할 값이 전 위치보다 높으면 높이 그 차이값 가중치 추가
    #최소비용 비교
    print(f'#{testcase} {minimum()}')


'''
3
3
0 2 1
0 1 1
1 1 1
'''