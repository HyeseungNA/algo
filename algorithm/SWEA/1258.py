def garo(y,x):
    global MAP,N
    d=0
    cnt1 = 0
    while MAP[y][x+d]!=0:
        if x+d >N-1:break
        d+=1
        cnt1+=1
    return cnt1
def sero(y,x):
    global MAP,N
    m = 0
    cnt2 = 0
    while MAP[y+m][x]!=0:
        if y+m > N-1:break
        m += 1
        cnt2 += 1
    return cnt2
def change(st_y,st_x,ed_y,ed_x):
    for i in range(st_y,ed_y):
        for j in range(st_x,ed_x):
            MAP[i][j] = 0
T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    lst = []
    MAP = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if MAP[i][j] !=0:
                w = garo(i,j)
                h = sero(i,j)
                lst.append([w,h])
                change(i,j,i+h,j+w)
    print(lst)
                    
'''
10
9
1 1 3 2 0 0 0 0 0
3 2 5 2 0 0 0 0 0
2 3 3 1 0 0 0 0 0
0 0 0 0 4 5 5 3 1
1 2 5 0 3 6 4 2 1
2 3 6 0 2 1 1 4 2
0 0 0 0 4 2 3 1 1
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
'''   