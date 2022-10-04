#longest common string 코드
arr1 = 'BABJYP'
arr2 = 'ABCBJY'
n = len(arr1)
m = len(arr2)
MAX = -21e8
MAP = [[0]*(n+1) for _ in range(m+1)]
for i in range(m):
    for j in range(n):
        #전 대각선 값 누적합
        if arr1[i] == arr2[j]:
            MAP[i+1][j+1] = MAP[i][j] + 1
            if MAX < MAP[i+1][j+1]:
                MAX = MAP[i+1][j+1]
print(MAX)

#longest common subquence
arr1 = 'BABJYP'
arr2 = 'ABCBJY'
n = len(arr1)
m = len(arr2)
MAX = -21e8
MAP = [[0]*(n+1) for _ in range(m+1)]
for i in range(m):
    for j in range(n):
        #전 대각선 값 누적합
        if arr1[j] == arr2[i]:
            MAP[i+1][j+1] = MAP[i][j] + 1
        else:
            MAP[i+1][j+1]= max(MAP[i+1][j],MAP[i][j+1])
        if MAX < MAP[i+1][j+1]:
            MAX = MAP[i+1][j+1]
print(MAX)


#longest increasing subquence
arr = [10,20,10,30,20,50]
result = [1] * 6
for i in range(6):
    for j in range(6):
        if arr[i] > arr[j] and result[i] < result[j]+1:
            result[i] = result[j] + 1
print(max(result))
#floyd warshell

inf = int(21e8)
arr = [[0,5,inf,8],
       [7,0,9,inf],
       [2,inf,0,4],
       [inf,inf,3,0]
       ]
for k in range(4):  # k는 경유지
    for i in range(4): # i는 시작점
        for j in range(4): # j는 도착점
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

for m in range(4):
    for n in range(4):
        print(arr[m][n],end = ' ')
    print()