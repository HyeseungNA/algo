T = int(input())
for testcase in range(1,T+1):
    card = list(input())
    arr = ['S','D','H','C']
    for m in range(4):
        bucket = [0] * 14
        for i in range(len(card)//3):
            for j in range(i*3,i*3 + 3):
                if arr[j][0] == arr[m]:
                    print(arr[j][0])
                    bucket[int(str(card[j][1])+ str(arr[j][2]))] += 1
        cnt = 0
        for l in range(1,len(bucket)):
            if bucket[l] == 0:
                cnt +=1
                print(cnt,end = '')
            if bucket[l] > 1:
                print('ERROR')
                break
        
                    
            
                
        

'''
3
S01D02H03H04
'''