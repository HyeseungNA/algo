def dfs(now,level,sum):
    global arr,MAX
    if level == 5:
        if MAX < sum:
            MAX = sum
        return 

    direct = [-1,0,1]
    for i in range(3):
        dy = level
        dx = now + direct[i]
        if dx < 0 or dx > 3:continue
        if arr[dy][dx] == 0:continue
        dfs(dx,level+1,sum+arr[dy][dx])
    
arr = [
    [3,2,4,1],
    [0,1,0,5],
    [2,0,3,0],
    [5,4,0,2],
    [2,-5,0,3]
]
MAX = 0
#첫 시작점 잡기
for i in range(4):
    dfs(i,0,0) 
print(MAX)
