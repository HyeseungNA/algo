T = int(input())
for testcase in range(1,T+1):
    card = list(input())
    arr = ['S','D','H','C']
    k = len(card)
    flag = 0
    print(f'#{testcase}',end = ' ')
    
    cnts= []
    for m in range(4):
        bucket = [0] * 14
        for i in range(0,k,3):
            if card[i] == arr[m]:
                bucket[int(card[i+1]+ card[i+2])] += 1
 
        cnt = 0
        for l in range(1,len(bucket)):      
            if bucket[l] > 1:
                flag = 1
                break
            if bucket[l] == 0:
                cnt +=1
        cnts.append(cnt)     
        
    
    if flag == 1:
        print('ERROR')
    else:
        print(*cnts)
        
        
    

'''
1
H02H10S11H02
'''