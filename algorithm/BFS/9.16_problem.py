# from collections import deque
# q = deque()
# q.append(2)
# q.append(4)
# q.append(9)
# print(*q)
# q.appendleft(5)
# print(*q)
# x = q.popleft()
# print(*q)


# # A B C D E F BFS로 구현하기
# arr = list(input().split())
# arr2 = [[0,1,0,1,0,0],
#         [0,0,1,0,1,0],
#         [0,0,0,0,0,0],
#         [0,0,0,0,0,1],
#         [0,0,0,0,0,0],
#         [0,0,0,0,0,0],

# ]
# def bfs(st):
#     global answer
#     q = deque()
#     q.append(st)
#     while q:
#         now = q.poplefft()
#         answer.append(name[now])
#         for i in range(6):
#             if arr[now][i] == 1:
#                     q.append(i)
#                     used[i]=1
# bfs(0)
# print(*answer)



# #중복 없이 BFS 구현하기
# def bfs(st):
#     global answer
#     q = deque()
#     q.append(st)
#     while q:
#         now = q.popleft()
#         answer.append(name[now])
#         for i in range(4):
#             if arr[now][i] == 1:
#                 if used[i] == 0:
#                     q.append(i)
#                     used[i] = 1
  
# name = list(input().split())
# arr = [[0,1,1,0],
#        [0,0,1,1],
#        [0,1,0,1],
#        [0,0,0,0],
#         ]
# answer = []
# used = [0]*4
# used[1] = 1
# bfs(1)
# print(*answer)

# #개화시기 문제다 이놈들아
# n = int(input())
# y,x = map(int,input().split())
# arr = [[0]*n for _ in range(n)]

# def bloom(y,x):
#     global arr,n
#     arr[y][x] = 1
#     q = deque()
#     q.append([y,x])
#     while q:
#         now = q.popleft()
#         y,x = now[0],now[1]
#         dy = [-1,1,0,0]
#         dx = [0,0,1,-1]
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if 0 <= ny <n and 0<= nx <n:
#                 if arr[ny][nx] == 0:
#                     arr[ny][nx] = arr[y][x] +1
#                     q.append([ny,nx])


# bloom(y,x)
# for i in arr:
#     print(*i)





# #씨앗 두개받는 문제다 이놈들아,,
# def bfs(lst):
#     q = deque()
#     q.append(lst[0])
#     q.append(lst[1])
#     while q:
#         now = q.popleft()
#         y = now[0]
#         x = now[1]
#         dy = [-1,1,0,0]
#         dx = [0,0,-1,1]
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if 0 <= ny < n and 0 <=nx <n:
#                 if arr[ny][nx] == 0:
#                     day = arr[y][x]
#                     arr[ny][nx] = arr[y][x] +1
#                     q.append([ny, nx])
#     return day
    
# n = int(input())
# arr = [[0]*n for _ in range(n)]
# lst = [list(map(int,input().split())) for _ in range(2)]
# for i in range(2):
#     y,x = lst[i]
#     arr[y][x] = 1
# print(bfs(lst))
# for i in arr:
#     print(*i)



# #씨앗 개화시기
# from collections import deque
# n= int(input())
# y,m = map(int,input().split())
# arr = [[0]*n for _ in range(n)]
# def bfs(y,x,level):



# bfs(y,x,0)


from collections import deque
n=int(input()) # map 사이즈 입력
y,x=map(int,input().split()) # 시작점 입력
arr=[[0]*n for _ in range(n)]

arr[y][x]=1
q=deque()
q.append((y,x,0))

answer=0
while q:
    y,x,level=q.popleft()
    if y==0 and x==0: answer=level
    directy=[0,0,1,-1]
    directx=[1,-1,0,0]
    for i in range(4):
        dy=y+directy[i]
        dx=x+directx[i]
        if 0<=dy<n and 0<=dx<n:
            if arr[dy][dx]==0:
                arr[dy][dx]=arr[y][x]+1
                q.append((dy,dx,level+1))
                # if dy==0 and dx==0:
                #     answer=level+1



for i in arr:
    print(*i)
print(answer)

'''
test case
5
3 1
'''
# # 화단에 꽃이 모두 개화하는데 몇 일이 걸릴지 출력하라
# from collections import deque
# def bfs(lst):
#     global arr
#     q = deque()
#     for i in range(len(lst)):
#         q.append(lst[i])
#     while q:
#         now = q.popleft()
#         y, x = now
#         dy = [0,1,0,-1]
#         dx = [1,0,-1,0]
#         for i in range(4):
#             ny, nx = y+dy[i], x+dx[i]
#             if ny>n-1 or nx>n-1 or ny<0 or nx<0: continue
#             if arr[ny][nx] != 0: continue
#             arr[ny][nx] = arr[y][x]+1
#             days=arr[y][x]
#             q.append([ny, nx])
#     return days

# n = int(input())
# lst = [[1,3],[5,6]]
# arr = [[0]*n for _ in range(n)]
# for y, x in lst:
#     arr[y][x]=1

# print(f'{bfs(lst)}일 후')
# # for i in range(n): # 그래프 출력
# #     print(*arr[i])

