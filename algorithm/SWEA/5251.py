def findboss(member):
    if lst[member] == member:
        return member
    ret = findboss(lst[member])
    return ret

def union(a,b):
    global result
    aboss= findboss(a)
    bboss = findboss(b)   
    if aboss == bboss:
        return
    if aboss != bboss:
        lst[bboss] = aboss       
        
T = int(input())
for testcase in range(1,T+1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    lst = list(range(N+1))
    result = []
    for i in range(M):
        a = arr[2*i]
        b = arr[2*i+1]
        union(a,b)     
    for j in range(1,N+1):
        if findboss(j) not in result:
            result.append(findboss(j))
    # print(result)
    print(f'#{testcase} {len(result)}')

'''
3
5 2
1 2 3 4
'''