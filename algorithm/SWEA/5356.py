T = int(input())
for testcase in range(1,T+1):
    arr = [list(input()) for _ in range(5)]
    result = [['_']*15 for _ in range(5)]
    ans = ''
    for i in range(5):
        for j in range(len(arr[i])):
            result[i][j] = arr[i][j]
    
    for m in range(15):
        for n in range(5):
            if result[n][m] !='_':
                ans+=result[n][m]
    print(f'#{testcase} {ans}')
'''
2
ABCDE
abcde
01234
FGHIJ
fghij
'''