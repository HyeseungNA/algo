def garo(y,x):
    d = 0
    cnt = 0
    while 1:
        if x+d > N-1:
            break
        if MAP[y][x+d] ==0:
            break
        if MAP[y][x+d] !=0:
            cnt += 1
        d += 1
    return cnt


def sero(y,x):
    m = 0
    cnt2 = 0
    while 1:
        if y+m > N-1:
            break
        if MAP[y+m][x] ==0:
            break
        if MAP[y+m][x] !=0:
            cnt2+=1
        m+=1
    return cnt2
    
def changeMAP(st_y,st_x,ed_y,ed_x):
    for a in range(st_y,ed_y):
        for b in range(st_x,ed_x):
            MAP[a][b] = 0

T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    MAP = [list(map(int,input().split())) for _ in range(N)]
    lst = []
    for i in range(N):
        for j in range(N):
            if MAP[i][j] != 0:
                w = garo(i,j)
                h = sero(i,j)
                changeMAP(i,j,i+h,j+w)
                lst.append([w*h,w,h])
    lst.sort(key=lambda x:(x[0],x[2]))
    print(f'#{testcase} {len(lst)}',end = ' ')
    for k in range(len(lst)):
        print(lst[k][2],lst[k][1],end = ' ')
    print()
            
