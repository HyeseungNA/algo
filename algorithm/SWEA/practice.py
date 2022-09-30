T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    Max = 0
    for i in range(1,N-1):
        gop = 1
        for j in range(i+1,N):
            gop = lst[i] * lst[j]
            if gop > Max and gop%(10**(len(str(gop))-1)) > gop//(10**(len(str(gop))-1)):
                Max = gop
    if Max !=0: print(f"#{tc} {Max}")
    else: print(f"#{tc} 0")


'''
1
4
2 4 7 10
'''

T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    arr = list(map(int, input().split()))
    path = [0]*2
    MAX = 0
    multiples = []
    def rcr(level, start, total):
        if level == 2:
            multiples.append(total)
            return

        for i in range(start, len(arr)):
            rcr(level+1, i+1, total*arr[i])


    rcr(0, 0, 1)
    multiples = sorted(multiples, key=lambda x: x)

    # print(multiples)

    flg_cnt =0
    for i in range(len(multiples)):
        flg = 0
        multiples[i] = str(multiples[i])
        for j in range(len(multiples[i])-1):
            if multiples[i][j]<=multiples[i][j+1]:
                continue
            else:
                flg = 1
                flg_cnt +=1
                break

        if flg == 0:
            multiples[i]=int(multiples[i])
            if multiples[i]>MAX:
                MAX = multiples[i]

    if flg_cnt ==len(multiples)-1:
        MAX = -1


    print(f'#{tc} {MAX}')