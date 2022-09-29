def bomb(y,x):
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    for m in range(4):
        index = 1
        while(1):
            ny = y + (dy[m] * index) 
            nx = x + (dx[m] * index)      
            if ny < 0 or nx < 0 or ny > 4 or nx > 4 or arr[ny][nx] == 3:
                break
            if arr[ny][nx] == 0:
                arr[ny][nx] = 2 # 안전지대를 바꿔주기            
            index += 1
        
arr = [[0,0,3,0,0],
       [0,3,1,0,3],
       [0,3,1,0,3],
       [3,0,0,1,0],
       [0,3,1,0,3],
        ]
for i in range(5):
    for j in range(5):
        if arr[i][j] == 1: #폭탄 인덱스 불러오기
            bomb(i,j)
cnt = 0
for m in range(5):
    for n in range(5):
        if arr[m][n] == 0:
            cnt += 1

print(cnt)

# if TRUE or (False):
#True

#if False or True:
#True

#if True and False:
#False

#if False and (True):
#False

#if True or (True):
#True