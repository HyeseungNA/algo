T = int(input())
for testcase in range(1,T+1):
    arr = input()
    arr = arr.replace('()','ㅣ')
    pole = 0
    cut = 0
    
    for i in arr:
    #'('를 만나면 쇠막대기 추가
        if i == '(':
            pole += 1
    #')'를 만나면 쇠막대기 한개 제거, 조각 한개 추가
        elif i == ')':
            pole -= 1
            cut += 1
    # 레이저를 만나면 쇠막대기 수 만큼 조각 추가
        elif i == 'ㅣ':
            cut += pole
        
    print(f'{testcase} {cut}')
    




'''
2
()(((()())(())()))(())
'''