def garo(y,x):
    d = 0
    cnt1 = 0
    while arr[y][x+d]!=0:
        cnt1+=1
        d+=1
    return cnt1

def sero(y,x):
    m= 0
    cnt2 = 0
    while arr[y+m][x] !=0:
        m+=1
        cnt2+=1
    return cnt2

def change(st_x,st_y,ed_x,ed_y):
    for yy in range(st_y,ed_y):
        for xx in range(st_x,ed_y):
            MAP[yy][xx] = 0  

T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    MAP = list(int,input().split())
    lst = []
    for i in range(N):
        for j in range(N):
            if MAP[i][j] !=0:
                w = garo(i,j)
                h= sero(i,j)
                lst.append([h,w])
                change(i,j,i+h,j+w) #y 시작 인덱스,x 시작 인덱스, y 끝 인덱스, x 끝인덱스
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