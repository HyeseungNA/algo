T = int(input())
for testcase in range(1,T+1):
    tc, n = input().split()
    arr = list(input().split())
    dict = {'ZRO':0,'ONE':1,'TWO':2,'THR':3,'FOR':4,'FIV':5,'SIX':6,'SVN':7,'EGT':8,'NIN':9}
    arr.sort(key=lambda x:dict[x])  
    print(tc)
    result = ' '.join(arr)
    print(result)