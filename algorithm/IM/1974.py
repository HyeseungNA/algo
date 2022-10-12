T = int(input())
for testcase in range(1,T+1):
    puzzle = [list(map(int,input().split())) for _ in range(9)]
    flag = 1
    #가로 탐색
    for i in range(9):
        total = 0
        for j in range(9):
            total += puzzle[i][j] 
        if total != 45:
            flag = 0
            break
    #세로 탐색
    for i in range(9):
        total = 0
        for j in range(9):
            total += puzzle[j][i]
        if total != 45:
            flag = 0
            break

    #사각형 탐색
    for i in range(0,9,3):
        total = 0
        for y in range(i,i+3):
            for x in range(i,i+3):
                total += puzzle[y][x]
        if total != 45:
            flag = 0
            break
    
    if flag == 0:
        print(f'#{testcase} 0')
    else:
        print(f'#{testcase} 1')

T = int(input())
for testcase in range(1,T+1):
    puzzle = [list(map(int,input().split())) for _ in range(9)]
    flag = 1
    # 가로 탐색
    for i in range(9):
        lst = []
        for j in range(9):
            lst.append(puzzle[i][j])
        if len(set(lst)) != 9:
            flag = 0
            break


    #세로 탐색
    for i in range(9):
        lst = []
        for j in range(9):
            lst.append(puzzle[j][i])
        if len(set(lst)) != 9:
            flag = 0
            break
    
    #사각형 탐색
    for i in range(0,9,3):
        lst = []
        for m in range(i,i+3):
            for n in range(i,i+3):
                lst.append(puzzle[m][n])
        if len(set(lst)) != 9:
            flag = 0
            break

    if flag == 0:
        print(f'#{testcase} 0')
    else:
        print(f'#{testcase} 1')
    