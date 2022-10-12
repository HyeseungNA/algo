T = int(input())
for testcase in range(1,T+1):
    arr = input()
    arr =  arr.replace('()','ㅣ')
    bole = 0
    stick = 0
    for i in arr:
        if i == '(':
            bole +=1
        
        elif i == ')':
            bole-=1
            stick +=1
        
        else:
            stick += bole
    print(f'#{testcase} {stick}')


    

'''
2
()(((()())(())()))(())
'''