def dfs(level,sum):
    global arr,MAX
    if level == 4:
        if sum> MAX:
            MAX = sum
        return 

    for i in range(3):
        dfs(level+1,sum+arr[level][i])
arr = [
    [2,5,7],
    [8,4,-8],
    [-7,1,4],
    [5,1,9]
]
MAX = 0
dfs(0,0)
print(MAX)