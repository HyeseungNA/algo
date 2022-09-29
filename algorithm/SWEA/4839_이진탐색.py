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
    cnts = [0]*2
    for i in range(2):
        cnts[i] = binary_search(1, arr[0],arr[i+1])

    print(f'#{testcase}',end = ' ')
    if cnts[0] < cnts[1]:
        print('A')
    elif cnts[0] == cnts[1]:
        print(0)
    else:
        print('B')



'''
3
400 300 350
1000 299 578
1000 222 888

1
1 1 1
'''



    
