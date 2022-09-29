T = int(input())
for testcase in range(1,T+1):
    t,length = input().split()
    arr = list(input().split())
    ans = []
    num = ['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']
    for i in range(len(num)):
        for j in range(len(arr)):
            if num[i] == arr[j]:
                ans.append(arr[j])
    print(f'#{testcase}')
    print(*ans)




T = int(input())
 
for tc in range(1, T+1):
    t, case_number = input().split()
    case_number = int(case_number)
    arr = list(input().split())
 
    names = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    ans = []
    for a in range(len(names)):
        for i in range(len(arr)):
            if names[a] == arr[i]:
                ans.append(arr[i])
 
    print(f'#{tc}')
    for j in range(len(ans)):
        print(ans[j], end= ' ')