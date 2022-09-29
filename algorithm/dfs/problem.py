
# def abc(level,sum):
#     global cnt
#     if level == n:
#         if sum ==10:
#             cnt+=1
#         return


#     for i in range(1,5):
#         abc(level+1,sum+i)


# n = int(input())
# cnt= 0
# abc(0,0)
# print(cnt)




# 4명이 놀이동산에 갔습니다. [M B T I]
# 놀이기구를 타는데 1 unit에 3명이 앉을 수 있습니다.
# 4명중에 1명이 고소공포증이 있어서 놀이기구를 안탄다고 합니다.
# 놀이기구를 탈 조합을 모두 출력해 주세요.


# def dfs(level,st):
#     if level==3:
#         for i in range(3):
#             print(path[i],end = '')
#         return

#     for i in range(st,4):
#         if used[i]==0:
#             path[level]=arr[i]
#             dfs(level+1,i+1)
#             used[i] = 0
#             path[level] = 0
       
# arr = ['M','B','T','I']
# path= ['']*3
# used = [0]*4
# dfs(0,0) #level,st


# def dfs(level,sum):
#     global MIN,used1,used2
#     if level == 12:
#         return
#         if MIN > abs(sum):
#             MIN = abs(sum)


#     if level %2 ==0:
#         for i in range(6):
#             if used1[i] == 0:
#                 used1[i] = 1
#                 dfs(level+1,sum+line1[i]*level+1)
#                 used1[i] = 0

#     else:
#         for i in range(6):
#             if used2[i] == 0:
#                 used2[i] = 1
#                 dfs(level+1,sum+line2[i]*level+1)
#                 used2[i]= 0

# line1 = [3,7,1,-3,-6,1]
# line2 = [7,-4,1,-5,3,2]
# used1 = [0]*6
# used2 = [0]*6
# MIN = 100000
# dfs(0,0)
# def dfs(level, tot):
#     global min_tot
#     if level == len(power)-1 : return
#     if abs(total - 2*tot) < abs(total - 2*min_tot):
#         min_tot = tot
#     for i in range(len(power)):
#         if used[i]==1: continue
#         used[i]=1
#         dfs(level+1, tot+power[i])
#         used[i]=0

# power = [50, 40, 99, 5, 25, 6, 37]
# total = sum(power)
# min_tot = float('inf')
# used = [0]*len(power)
# dfs(0, 0)
# print(abs(total-2*min_tot))




# 조합
# def dfs(level, start, path): # path: 지나온 경로
#     global result
#     if level==3:
#         return

#     for i in range(start, 3):
#         backup = path
#         path = path+arr[i]
#         result.append(path)
#         dfs(level+1, i+1, path)
#         path = backup

# arr = ['A','B','C']
# result = []
# dfs(0,0,'')
# print(result)


# 중복조합
# def dfs(level, start, path): # path: 지나온 경로
#     global result
#     if level==3:
#         return

#     for i in range(start, 3):
#         backup = path
#         path = path+arr[i]
#         result.append(path)
#         dfs(level+1, i, path)
#         path = backup

# arr = ['A','B','C']
# result = []
# dfs(0,0,'')
# print(result)


# 순열
def dfs(level, path): # path: 지나온 경로
    global result
    if level==3:
        return

    for i in range(3):
        if used[i] == 0:
            backup = path
            result.append(path)
            used[i] = 1
            path = path+arr[i]
            dfs(level+1,path)
            used[i] = 0
            path = backup

arr = ['A','B','C']
result = []
used = [0]*3
dfs(0,'')
print(result)