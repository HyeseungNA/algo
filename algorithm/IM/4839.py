def binary_search(st,ed,target):
    cnt = 0
    while st <= ed:
        mid = (st+ed)//2
        cnt +=1
        if target == mid:
            return cnt
        if target < mid:
            ed = mid
        elif target > mid:
            st = mid

T = int(input())
for testcase in range(1,T+1):
    arr = list(map(int,input().split()))
    cnts = [0] * 2
    for i in range(2):
        cnts[i] = binary_search(1,arr[0],arr[i+1])

    
