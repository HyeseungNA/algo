T = int(input())
for testcase in range(1,T+1):
    N= int(input())
    farm = [list(map(int,input())) for _ in range(N)]
    st = N//2
    ed = N//2
    index = 0
    total = 0
    while index <=N-1:
        for j in range(st,ed):
            total += farm[index][j]
        if index <=N//2:
            st-=1
            ed+=1
        else: 
            st+=1
            ed-=1
        index+=1
    print(total)

'''
1
5
14054
44250
02032
51204
52212
'''