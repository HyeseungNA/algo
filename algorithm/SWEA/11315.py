#'O'인 지점 인덱스만 불러오기
# 벽에 닿거나 'O'가 아니면 끝내기
def omok(y,x):
    dy = [-1,1,0,0,-1,-1,1,1]#상하좌우대각선 탐색
    dx = [0,0,-1,1,-1,1,-1,1]
    for i in range(8):
        cnt = 1  # cnt는 1로 초기화
        while 1:
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or ny < 0 or nx > N-1 or ny > N-1: #벽에 닿으면 끝내브러,,
                break
            if arr[ny][nx] == '.':  # 오목 없으면 끝내브러,,
                break
            if arr[ny][nx] == 'o':  #오목 발견하면 카운트
                cnt += 1
        if cnt >= 5:  # 5개 이상이면 true 반환
            return True
    return False  # 5개 미만이면 false 반환


T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] =='o':
                if omok(i,j):
                    print(f'{testcase} YES')  # true면 yes 출력하고 끝내브러,,
                    break
    print(f'{testcase} NO')  # true 없으면 no출력
    


'''
1
5
....o
...o.
..o..
.o...
o....
'''
'''
4
5
.o.o.
o.o.o
.o.o.
o.o.o
.o.o.
'''