
def findboss(node):
    if arr[node] == node:
        return node
    ret = findboss(arr[node])
    return ret
def union(a,b):
    arr[bboss] = aboss    #연결해주기(b의 부모를 a로)

T = int(input())
for testcase in range(1,T+1):
    V,E = map(int,input().split())
    lst = [list(map(int,input().split()))for _ in range(E)]
    arr = list(range(1001))
    cost = 0
    lst.sort(key = lambda x:x[2]) # 비용 기준으로 정렬해주기
    for i in range(E):
        aboss = findboss(lst[i][0])  # 보스 찾기
        bboss = findboss(lst[i][1])
        if aboss != bboss:  #보스가 다르면 연결해주고 비용 더해주기
            union(lst[i][0],lst[i][1])
            cost += lst[i][2]  
                      
    print(f'#{testcase} {cost}')
            
        


'''
3
2 3
0 1 1
0 2 1
1 2 6
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
'''