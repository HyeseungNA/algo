# # import heapq

# # arr = []

# # heapq.heappush(arr, 4)    #최소합 디폴트 --> 값이 가장 작은 것이 우선순위가 높음
# # heapq.heappush(arr, 15)
# # heapq.heappush(arr, 2)
# # heapq.heappush(arr, 7)
# # heapq.heappush(arr, 5)
# # heapq.heappush(arr, 9)


# # print(heapq.heappop(arr))  # longn 속도로 우선순위가 가장 높은 값을 출력
# # print(heapq.heappop(arr))
# # print(heapq.heappop(arr))
# # print(heapq.heappop(arr))
# # print(heapq.heappop(arr))
# # print(heapq.heappop(arr))

# # for i in range(len(arr)):
# #     print(heapq.heappop(arr),end = ' ')
# import heapq
# arr = [4,87,4,24,8,23,3,7,4]

# # heapq.heappush(arr, 4)
# # heapq.heappush(arr, 87)
# # heapq.heappush(arr, 4)
# # heapq.heappush(arr, 24)
# # heapq.heappush(arr, 8)
# # heapq.heappush(arr, 23)
# # heapq.heappush(arr, 3)
# # heapq.heappush(arr, 7)
# # heapq.heappush(arr, 4)

# # for i in range(len(arr)):
# #     print(heapq.heappop(arr),end = ' ')

# heap = []
# for i in range(len(arr)):
#     heapq.heappush(heap, arr[i])

# for i in range(len(arr)):
#     print(heapq.heappop(arr[i]))

# heap = []
# heapq.heapify(arr): # arr 리스트를 한번에 heap 자료형을 바꾸기
# for i in range(len(arr)):
#     print(heapq.heappop(arr))

# heap = []
# for i in range(len(arr)):
#     heapq.heappush(heap, -arr[i]) #-87,-24,-23

# for i in range(len(arr)):
#     print(heapq.heappop(heap)*-1)
#     #print(-heapq.heappop(heap))


# #########################################
# import heapq
# arr=[4,87,4,24,8,23,3,7,4]  # max heap
# # 튜플
# heap=[]
# for i in range(len(arr)):
#     heapq.heappush(heap,(-arr[i],arr[i]))

# for i in range(len(arr)):
#     print(heapq.heappop(heap)[1])
# ###################################################

# import heapq
# arr=[4,87,4,24,8,23,3,7,4]  # max heap

# rev=lambda x:x*-1

# heap1=list(map(rev,arr))

# heapq.heapify(heap1) # heap 의 형태로 저장

# for i in range(len(arr)):
#     print(-heapq.heappop(heap1))


#카드 정렬하기 문제
# n = int(input())
# heap = []

# #정렬
# for _ in range(n):
#     heapq.heappush(card,int(input()))
# #출력
# answer = 0
# while len(card) > 1:
#     temp1 = heapq.heappop(card)
#     temp2 = heapq.heappop(card)
#     answer += (temp1+temp2)
#     heapq.heappush(card,temp1+temp2)



# name='ABCDE'
# inf=int(21e8)
# arr=[
#     [0,3,inf,9,5],
#     [inf,0,7,inf,1],
#     [inf,inf,0,1,inf],
#     [inf,inf,inf,0,inf],
#     [inf,inf,1,inf,0],
# ]
# used=[0]*5
# result=[0,3,inf,9,5]
# used[0]=1 # 시작점 'A'라고 가정함


# def select_ky():
#     Min=int(21e8)
#     Minindex=0;
#     for i in range(1,5):
#         if(used[i]==0 and result[i]<Min):
#             Min=result[i]
#             Minindex=i;
#     return Minindex

# def dijkstra():
#     for i in range(4):
#         via=select_ky() # 경유지 선택
#         used[via]=1
#         for j in range(5): # 모든 정점에 대한 비용을 비교
#             baro=result[j]  # 시->도
#             ky=result[via]+arr[via][j] # 시->경->도
#             if baro>ky:
#                 result[j]=ky
# dijkstra()
# print(*result)

def key_selected():
    MIN = 21e8
    MINIDX = 0
    for i in range(1,5):
        if used[i] == 0 and MIN > result[i]:
            MIN = result[i]
            MINIDX = i
    return MINIDX

def dijkstra():
    for _ in range(4):
        ky = key_selected()
        used[ky] = 1
        for j in range(5):
            baro = result[j]
            stop = result[ky] + arr[ky][j]
            if baro > stop:
                result[j] = stop
name='ABCDE'
inf=int(21e8)
arr=[
    [0,3,inf,9,5],
    [inf,0,7,inf,1],
    [inf,inf,0,1,inf],
    [inf,inf,inf,0,inf],
    [inf,inf,1,inf,0],
]
used=[0]*5
result=[0,3,inf,9,5]
used[0]=1 # 시작점 'A'라고 가정함

dijkstra()
print(*result)


