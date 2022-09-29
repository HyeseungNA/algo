def dfs(now):
    global cnt
    if name[now] == 'E':
        cnt +=1
    for i in range(5):
        if arr[now][i] == 1 and used[i] == 0:
            used[i] = 1
            dfs(i)
            used[i] = 0

name = ['A','B','C','D','E']
st = input()
arr = [[0,1,0,0,0],
       [0,0,1,1,1],
       [1,0,0,1,0],
       [0,0,0,0,1],
       [0,0,0,0,0],
    ]
used = [0]*5
cnt = 0
for i in range(5):
    if name[i] == st:
        st_idx = i
        used[st_idx] = 1
        dfs(st_idx)
print(cnt)