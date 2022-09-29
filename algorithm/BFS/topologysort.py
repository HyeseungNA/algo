from collections import deque

name=['cs','language','datastructure','algorithm','project','codingtest','to be a programmer']

map = [
    [0,0,0,0,0,0,1],
    [0,0,1,1,0,0,0],
    [0,0,0,0,0,1,0],
    [0,0,0,0,0,1,0],
    [0,0,0,0,0,0,1],
    [0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0],
]


arr = [0]*7
used = [0]*7
q = deque()
for i in range(7):
    for j in range(7):
        if map[j][i] == 1:
            arr[i] += 1

for i in range(7):
    if arr[i] == 0:
        used[i] = 1
        q.append(i)


while q:
    now = q.popleft()
    print(name[now])
    for i in range(7):
        if map[now][i] == 1 and used[i] == 0:
            if arr[i] == 1:
                used[i] = 1
                arr[i]-=1
                q.append(i)
            else:
                arr[i]-=1


