T = int(input())
for testcase in range(1,T+1):
    N,M,K = map(int,input().split())
    waiting = list(map(int,input().split()))
    waiting.sort()
    for i in range(len(waiting)):
        boong = (waiting[i]//M) * K
        remain = boong - (i+1)
        if remain < 0:
            print(f'#{testcase} Impossible')
            break
    else:
        print(f'#{testcase} Possible')
        

'''
4
2 2 2
3 4
'''