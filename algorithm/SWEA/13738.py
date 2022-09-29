# def ispattern(i): # True/False
#     for j in range(len(str1)):
#         if str1[j] != str2[i+j]:
#             return False
#     return True 
    

# T = int(input())
# for testcase in range(1,T+1):
#     str1 = list(input())
#     str2 = list(input())
#     for i in range(len(str2)-len(str1)+1):
#         if ispattern(i):
#             print(f'#{testcase} 1')
#             break
#     else:
#         print(f'#{testcase} 0')

T = int(input())
for testcase in range(1,T+1):
    str1 = list(input())
    str2 = list(input())
    
    for i in range(len(str2)-len(str1)+1): # 0~6
        flag = 1
        for j in range(len(str1)): # 0~3
            if str1[j] != str2[i+j]:
                flag = 0
                break
        if flag:
            break
    print(f'#{testcase} {flag}')


'''
3
XYPV
EOGGXYPVSY
STJJ
HOFSTJPVPP
ZYJZXZTIBSDG
TTXGZYJZXZTIBSDGWQLW
'''