def increase(number):
    numbers = str(number) #문자열로 변환
    for m in range(len(numbers)-1):
        if numbers[m] > numbers[m+1]:
            return False
    return True

T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    MAX = -1
    for i in range(N-1):
        for j in range(i+1,N):
            num = arr[i] * arr[j]  # 숫자들 곱한 값을 보내주기
            if increase(num):
                if MAX < num:
                    MAX = num
    print(f'#{testcase} {MAX}')
    
    
                




    
        
'''
1
4
2 4 7 10
'''