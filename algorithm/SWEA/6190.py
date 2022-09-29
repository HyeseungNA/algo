def increase(multi):
    compare = str(multi)
    for m in range(len(compare)-1):
        if compare[m] > compare[m+1]:
            return False
    return True

T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    MAX = -1
    for i in range(N-1):
        for j in range(i+1,N):
            multi = arr[i] * arr[j]
            if increase(multi):
                if MAX < multi:
                    MAX = multi
    
    print(MAX)            
                
    
                




    
        
'''
1
4
2 4 7 10
'''