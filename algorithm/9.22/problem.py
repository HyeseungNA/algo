
#편의점
# n = int(input())
# arr = list(map(int,input().split()))
# arr.sort()
# total = 0
# lst= []
# for i in range(n):
#     total += arr[i]
#     lst.append(total)
# print(sum(lst))
# n= int(input())
# arr = list(map(int,input().spit()))
# arr.sort(reverse = True)
# total = 0
# for i in range(1,n+1):
#     total += (i*arr[i-1])

# print(total)

# 예약손님
# N = int(input())
# lst =[list(map(int,input().split())) for _ in range(N)]
# lst.sort(key = lambda x:x[1])
# cnt = 0
# before_time = -1
# for i in range(N):
#     if before_time <= lst[i][0]:
#         before_time = lst[i][1]
#         cnt+= 1
# print(cnt)
# arr = [[0,1,1,9],
#        [4,2,2,3],
#        [1,3,4,1],
#        [3,7,8,0]
#        ]
# dp = [list(map(int,input().split()))for _ in range(4)]

#최단거리

arr = [[0,1,1,9],
       [4,2,2,3],
       [1,3,4,1],
       [3,7,8,0]]

map = [[0]*4 for _ in range(4)]
for i in range(1,4):
    map[0][i] = arr[0][i] + map[0][i-1]
    map[i][0] = arr[i][0] + map[i-1][0]
for i in range(1,4):
    for j in range(1,4):
        map[i][j] = min(map[i-1][j]+arr[i][j],map[i][j-1]+arr[i][j])

print(map[3][3])   



