def findboss(member):
    if arr[member] == member:
        return member
    ret = findboss(arr[member])
    return ret
     
def union(a,b,cost):
    global ans
    aboss = findboss(a)
    bboss = findboss(b)
    if aboss != bboss:
        arr[bboss] = aboss
        ans += cost
     
         
 
T = int(input())
for testcase in range(1,T+1):
    V,E = map(int,input().split())
    arr = list(range(V+1))
    ans = 0
    lst = [list(map(int,input().split())) for _ in range(E)]
    lst.sort (key = lambda x:x[2])
    for i in range(E):
        a,b,cost = lst[i]
        union(a,b,cost)
    print(f'#{testcase} {ans}')

'''
3
2 3
0 1 1
0 2 1
1 2 6
'''