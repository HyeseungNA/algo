T = int(input())
 
for test_case in range(1, T+1):
 
    H, W = map(int,input().split())
    arr = []
 
    for i in range(H):
        arr.append(list(input()))
 
    N = int(input())
    user = list(input())
    i, j, idx = 0, 0, 0
    dx, dy = 0, 0
 
    for a in range(H):
        for b in range(W):
            s = arr[a][b]
            if s =='^' or s == '<' or s =='>' or s=='v':
                i, j = a, b
                break
        if s == ' ^' or s == '<' or s == '>' or s == 'v': break
 
    while idx < len(user):
        s = user[idx]
 
        if s == 'S':
            if arr[i][j] == '^':
                for k in range(i,-1,-1):
                    if arr[k][j] == '*':
                        arr[k][j] = '.'
                        break
                    elif arr[k][j] == '#':
                        break
            elif arr[i][j] == 'v':
                for k in range(i,H):
                    if arr[k][j] == '*':
                        arr[k][j] = '.'
                        break
                    elif arr[k][j] == '#':
                        break
            elif arr[i][j] == '>':
                for k in range(j, W):
                    if arr[i][k] == '*':
                        arr[i][k] = '.'
                        break
                    elif arr[i][k] == '#':
                        break
            elif arr[i][j] == '<':
                for k in range(j,-1,-1):
                    if arr[i][k] =='*':
                        arr[i][k] = '.'
                        break
                    elif arr[i][k] == '#':
                        break
        elif s == 'U':
            if i > 0 and arr[i-1][j] == '.':
                arr[i][j] = '.'
                i-=1
            arr[i][j] = '^'
        elif s == 'R':
            if j < W-1 and arr[i][j+1] == '.':
                arr[i][j] = '.'
                j+=1
            arr[i][j] = '>'
        elif s == 'L':
            if j > 0 and arr[i][j-1] == '.':
                arr[i][j] = '.'
                j-=1
            arr[i][j] = '<'
        elif  s == 'D':
            if i < H-1 and arr[i+1][j] == '.':
                arr[i][j] = '.'
                i += 1
            arr[i][j] = 'v'
 
        idx+=1
 
    print('#%d ' %(test_case),end ='')
    for i in range(H):
        for j in range(W):
            print(arr[i][j],end='')
        print(end='\n')