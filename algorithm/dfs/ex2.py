def dfs(now,SUM):
    global MIN
    if name[now] == "E":
        if SUM < MIN:
            MIN = SUM

    for i in range(5):
        if arr[now][i] >0 and used[i] == 0:
            used[i] = 1
            dfs(i,SUM+arr[now][i])
            used[i] = 0
            
name=['A','B','C','D','E']
st=input()  # 출발점 입력
MIN = 21e8
arr=[
    [0,4,0,0,0],
    [0,0,1,2,9],
    [5,0,0,7,0],
    [0,0,0,0,1],
    [0,0,0,0,0],
]
used=[0]*5
st_idx = 0
for i in range(5):
    if name[i] == st:
        st_idx = i
        break
used[st_idx] = 1
dfs(st_idx,0)
print(MIN)