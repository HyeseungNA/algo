def garo(direction):
    global arr,MAX
    for y in range(100):
        for i in range(100-direction+1):
            ans = ''
            for j in range(direction):
                ans += arr[y][i+j]
            ans_rev = ans[::-1]
            if ans_rev == ans:
                MAX < len(ans)
                MAX = len(ans)
    return MAX
        
def sero(direction):
    global arr,MAX
    for x in range(100):
        for i in range(100-direction+1):
            ans = ''
            for j in range(direction):
                ans += arr[i+j][x]
            ans_rev = ans[::-1]
            if ans_rev == ans:
                if MAX < len(ans):
                    MAX = len(ans)
    return MAX

for testcase in range(1,11):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]
    lst = []
    MAX = 0
    for i in range(1,101):
        ret1 = garo(i)
        ret2 = sero(i)
    print(f'#{testcase} {max(ret1,ret2)}')
    