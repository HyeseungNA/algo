arr = input()
def dfs(level,st):
    if level==3:
        for i in range(len(path)):
            print(path[i],end = '')
        print()
        return
    
    for i in range(st,len(arr)):
        path[level] = arr[i]
        dfs(level+1,i)

path = ['']*3
dfs(0,0)