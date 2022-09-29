N,M,x,y,K = map(int,input().split())
dy = [0,0,0,-1,1] #제자리,동,서,북,남
dx = [0,1,-1,0,0] #제자리,동,서,북,남
arr = [list(map(int,input().split())) for _ in range(N)]
orders = list(map(int,input().split()))
dice =[0]*6
for order in orders:
    ny = y + dy[order]
    nx = x + dx[order]
    if ny < 0 or nx < 0 or ny > N-1 or nx > M-1:continue
# 방향에 따라 주사위 인덱스 변경
# 위,아래,정면,후면,좌,우 = 0,1,2,3,4,5




    

