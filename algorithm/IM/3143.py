T = int(input())
for testcase in range(1,T+1):
    a,b = input().split()
    print(a.count(b))
'''
2
banana bana
'''
T = int(input())
for testcase in range(1,T+1):
    a,b = input().split()
    result = a.replace(b,'_')
    print(f'#{testcase} {len(result)}')