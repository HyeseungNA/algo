T = int(input())
for testcase in range(1,T+1):
    H,M = map(int,input().split())
    MAP = [list(input()) for _ in range(H)]
    N = int(input())
    arr = ['v','^','>','<'] #상하좌우
    order = list(input())
    for i in range(H):
        for j in range(M):
            if MAP[i][j] in arr:
                y = i
                x = j
    index = 0
    while index < N:
        st = order[index]
        if st == 'S':
            if MAP[y][x] == '^':
                for ny in range(y-1,-1,-1):
                    if MAP[ny][x] == '*':
                        MAP[ny][x] = '.' #벽돌을 만나면 평지로 만들어주고 break
                        break
                    elif MAP[ny][x] == '#':
                        break
            elif MAP[y][x] == 'v' : 
                for ny in range(y+1,H):
                    if MAP[ny][x] == '*':
                        MAP[ny][x] = '.'
                        break
                    if MAP[ny][x] == '#':
                        break
            elif MAP[y][x] == '<': 
                for nx in range(x-1,-1,-1):
                    if MAP[y][nx] == '*':
                        MAP[y][nx] = '.'
                        break
                    if MAP[y][nx] == '#':
                        break   
            elif MAP[y][x] == '>':
                for nx in range(x+1,M):
                    if MAP[y][nx] =='*':
                        MAP[y][nx] = '.'
                        break 
                    if MAP[y][nx] == '#':
                        break              
        elif st == 'U':
            if y > 0 and MAP[y-1][x] == '.':
                MAP[y][x] = '.'
                y = y-1
            MAP[y][x] = '^'
     
        elif st == 'L':
            if x > 0 and MAP[y][x-1] =='.':
                MAP[y][x] = '.'
                x = x-1
            MAP[y][x] = '<'
        elif st == 'D':
            if y < H-1 and MAP[y+1][x] == '.':
                MAP[y][x] = '.'
                y = y+1
            MAP[y][x] = 'v'
        
        elif st == 'R':
            if x < M-1 and MAP[y][x+1] == '.':
                MAP[y][x] = '.'
                x = x+1
            MAP[y][x] = '>'
        index += 1
    print(f'#{testcase}',end = ' ')
    for i in range(H):
        for j in range(M):
            print( MAP[i][j],end = '')
        print()
    print()
        
        
'''
1
3 7
***....
*-..#**
#<.****
23
SURSSSSUSLSRSSSURRDSRDS
'''