k = int(input()) # 정점의 갯수
n = int(input()) # 간선의 갯수
lst = [list(input().split()) for _ in range(n)]
lst.sort(key=lambda x:int(x[2])) 
costs = 0
arr = [0]*200

def union(a, b):
    global arr
    arr[ord(b)] = a

def find(x):
    global arr
    if arr[ord(x)] == 0:
        return x
    ret = find(arr[ord(x)])
    arr[ord(x)] = ret
    return ret

for i in range(n):
    a, b, cost = lst[i]
    fa, fb = find(a), find(b)
    if fa != fb:
        union(a, b)
        costs += int(cost)
print(costs)




'''
test case
5
8
C D 1
A B 9
A C 3
A E 7
B D 11
A D 20
B C 14
C E 5
'''


import sys
sys.stdin = open("input.txt", "r")
k=int(input()) # 정점개수
n=int(input()) # 간선개수
lst=[list(input().split())for _ in range(n)] # 간선의 정보 입력
lst.sort(key=lambda x:int(x[2]))

arr=[0]*200


def findboss(member):
    if arr[ord(member)]==0: return member
    ret=findboss(arr[ord(member)])
    arr[ord(member)]=ret
    return ret

def union(y,x,i):
    global answer,cnt
    yboss,xboss=findboss(y),findboss(x)
    if yboss==xboss: return
    answer+=int(lst[i][2])      # 비용 더하기
    cnt+=1                      # 간선의개수 더하기
    arr[ord(xboss)]=yboss

answer=0 # 비용을 더할 변수
cnt=0    # 간선의 개수를 더할 변수
for i in range(n):
    if cnt==k-1:     # cnt가 간선의 개수 -1 개와 같으면 
        print(answer)
        break
    union(lst[i][0],lst[i][1],i)