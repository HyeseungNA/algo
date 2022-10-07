# T = int(input())
# for testcase in range(1,T+1):
#     N = int(input())
#     arr = list(input().split())
#     a = []
#     b = []
#     total = []
#     if N%2 == 0:
#         mid = (N//2)
#         for i in range(N//2):
#             a.append(arr[i])
#         for i in range(N//2,N):
#             b.append(arr[i])
        
#         for j in range(N//2):
#             total.append(a[j])
#             total.append(b[j])
#     else:
#         mid = ((N//2)+1)
#         for i in range(N//2+1):
#             a.append(arr[i])
#         for i in range(N//2+1,N):
#             b.append(arr[i])
        
#         for j in range(N//2):
#             total.append(a[j])
#             total.append(b[j])
#         total.append(a[-1])
#     result = ' '.join(total)
#     print(f'#{testcase}',end = ' ')
#     print(result)
    
T = int(input())
for testcase in range(1,T+1):
    N= int(input())
    arr = list(input().split())
    lst = []
    total = []
    if N%2 == 0:
        mid = (N//2)
        for _ in range(mid):
            lst.append(arr.pop(0))
    else:
        mid = (N//2+1)
        for i in range(mid):
            lst.append(arr.pop(0))
    for j in range(N):
        if j%2==0:
            total.append(lst.pop(0))
        else:
            total.append(arr.pop(0))
    print(f'#{testcase}',*total,sep= ' ')
            
    

'''
3
6
A B C D E F
5
ALAKIR ALEXSTRASZA DR-BOOM LORD-JARAXXUS AVIANA
'''