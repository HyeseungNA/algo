for t in range(10):
    N = int(input())
    arr = [list(input()) for _ in range(100)]
    max = 0
    def check(y,x):
        global max
        checking = []
        for yy in range(y,100):
            checking.append(arr[yy][x])
            if checking == checking[::-1] and len(checking) > max:
                max = len(checking)
        checking = []
        for xx in range(x,100):
            checking.append(arr[y][xx])
            if checking == checking[::-1] and len(checking) > max:
                max = len(checking)
        return
 
    for y in range(100):
        for x in range(100):
            check(y,x)
    print(f"#{t+1} {max}")