# def isbaduk(y,x,color):
#     dy = [-1,1,0,0,-1,-1,1,1]
#     dx = [0,0,-1,1,-1,1,-1,1]
   
#     if color == 1:  #흑돌이면
#         for i in range(8):
#             lst = []
#             s_y = y
#             s_x = x
#             while 1:
#                 ny = s_y + dy[i]
#                 nx = s_x + dx[i]
#                 if nx < 0 or ny < 0 or nx > N-1 or ny > N-1: #범위를 벗어나면 리스트 초기화
#                     lst = []
#                     break
#                 if baduk[ny][nx] == 0: # 아무것도 없어도 초기화
#                     lst = []
#                     break
#                 if baduk[ny][nx] == 2: #다른색이면 리스트안에 넣기
#                     lst.append([ny,nx])
#                     s_y = ny
#                     s_x = nx
#                 if baduk[ny][nx] == 1:  # 같은 색을 만나면 이동 멈추기
#                     for r,c in lst:
#                         baduk[r][c] = 1
#                     break
                    
#     elif color == 2:  #흑돌이면
#         for i in range(8):
#             lst = []
#             s_y = y
#             s_x = x
#             while 1:
#                 ny = s_y + dy[i]
#                 nx = s_x + dx[i]
#                 if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:
#                     lst = []
#                     break
#                 if baduk[ny][nx] == 0:
#                     lst = []
#                     break
#                 if baduk[ny][nx] == 1:
#                     lst.append([ny,nx])
#                     s_y = ny
#                     s_x = nx
#                 if baduk[ny][nx] == 2:
#                     for rr,cc in lst:
#                         baduk[rr][cc] = 2
#                     break

# T = int(input())
# for testcase in range(1,T+1):
#     N,M = map(int,input().split())
#     baduk = [[0]*N for _ in range(N)]
#     baduk[(N-1)//2][(N-1)//2] = 2
#     baduk[(N-1)//2+1][(N-1)//2+1] =2
#     baduk[(N-1)//2][(N-1)//2+1] = 1
#     baduk[(N-1)//2+1][(N-1)//2] = 1
#     for _ in range(M):
#         x,y,color = map(int,input().split())
#         baduk[y-1][x-1] = color
#         isbaduk(y-1,x-1,color)
#     black = 0
#     white = 0
#     for m in range(N):
#         for n in range(N):
#             if baduk[m][n] ==2 :
#                 black += 1
#             elif baduk[m][n] ==1:
#                 white += 1
#     print(f'#{testcase} {white} {black}')
            

lst = [[1,2],[3,4],[5,6]]
for r,c in lst:
    print(r,c)