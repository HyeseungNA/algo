T = int(input())
for testcase in range(1,T+1):
    charge = int(input())
    money = [50000,10000,5000,1000,500,100,50,10]
    index = 0
    lst = []
    while index <= 7:
        cnt = charge//money[index]
        lst.append(cnt)
        charge-= cnt * money[index]
        index += 1
    result = ' '.join(map(str,lst))
    print(f'#{testcase}')
    print(result)
        
    