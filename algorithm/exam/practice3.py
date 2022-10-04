
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     attack = [list(map(int, input().split())) for _ in range(N)]
#     # 상하좌우의 직선방향으로 공격이 가능하므로, 4방향 델타 사용
#     # 상하좌우
#     dy = [-1, 1, 0, 0]  
#     dx = [0, 0, -1, 1]
#     r = 0
#     c = 0

#     # N*N으로 이중반복문을 돌려서 2인 방어탑 위치들을 찾기
#     # 해당하는 좌표를 r과 c에 저장한후 그 위치 기준에서 상하좌우이되
#     # 조건에 해당하는 (인덱스 벗어나지않아야고 중첩되는곳 고려) 곳들을 3으로 저장
#     for y in range(N):
#         for x in range(N):
#             if attack[y][x] == 2:
#                 r = x
#                 c = y
#                 for i in range(4):
#                     for k in range(1,20): #N이 최대 20이라고 문제에서 말해주었음
#                         rx = r + (k * dx[i]) 
#                         ry = c + (k * dy[i])
#                         if rx < 0 or ry < 0 or rx > N-1 or ry > N-1:
#                             break
#                         if attack[ry][rx] == 1 or attack[ry][rx] == 2:
#                             break
#                         if attack[ry][rx] == 0:
#                             attack[ry][rx] = 3
    
   
#                         # 문제에서 주어
#                         # 진 형광노랑펜 색들을 다 3으로 바꾼 상태임.

#     result = 0
#     for yy in range(N):
#         for xx in range(N):
#             if attack[yy][xx] == 0:  
#                 result += 1
#     print(f'#{tc} {result}')
    
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    attack = [list(map(int, input().split())) for _ in range(N)]
    # 상하좌우의 직선방향으로 공격이 가능하므로, 4방향 델타 사용
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    r = 0
    c = 0
    # N*N으로 이중반복문을 돌려서 2인 방어탑 위치들을 찾기
    # 해당하는 좌표를 r과 c에 저장한후 그 위치 기준에서 상하좌우이되
    # 조건에 해당하는 (인덱스 벗어나지않아야고 중첩되는곳 고려) 곳들을 3으로 저장
    for x in range(N):
        for y in range(N):
            if attack[x][y] == 2:
                r = x
                c = y
                for i in range(4):
                    for k in range(1,20): #N이 최대 20이라고 문제에서 말해주었음
                        rx = r + (k * dx[i])
                        ry = c + (k * dy[i])
                        if rx < 0 or ry < 0 or rx > N-1 or ry > N-1:
                            break
                        if attack[rx][ry] == 1 or attack[rx][ry] == 2:
                            break
                        if attack[rx][ry] == 0:
                            attack[rx][ry] = 3


                        # 문제에서 주어진 형광노랑펜 색들을 다 3으로 바꾼 상태임.

    result = 0
    for xx in range(N):
        for yy in range(N):
            if attack[xx][yy] == 0:
                result += 1
    print(f'#{tc} {result}')
'''
3
5
0 1 0 0 0
0 0 2 2 0
0 1 0 0 0
0 2 1 2 0
0 0 0 0 0


'''