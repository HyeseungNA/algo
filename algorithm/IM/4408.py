T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    cor = [0] * 400
    for _ in range(N):
        st,ed = map(int,input().split())
        if st > ed:
            st,ed = ed,st
        for i in range((st-1)//2,(ed-1)//2+1):
            cor[i]+=1
                
    print(f'#{testcase} {max(cor)}')
    
    

    
        


    