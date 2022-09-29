def iswinner(player):
    # 같은 숫자가 3개 이상일때
    for m in range(len(player)):
        if player[m] >= 3:
            return True

    # 연속된 숫자가 3개 이상일때
    for m in range(8):
        if player[m] > 0 and player[m+1] > 0 and player[m+2] > 0 :
            return True
    return False


T = int(input())
for testcase in range(1,T+1):
    cards = list(map(int,input().split()))
    p1 = [0]*10
    p2 = [0]*10
    ret = 0
    for i in range(len(cards)):
        #짝수일때 p1에 넣기
        if i % 2 == 0:
            p1[cards[i]] += 1
            if iswinner(p1):
                ret = 1
        #홀수일때 p2에 넣기
        elif i % 2 != 0:
            p2[cards[i]] += 1
            if iswinner(p2):
                ret = 2
    print(ret)
'''
3
9 9 5 6 5 6 1 1 4 2 2 1
5 3 2 9 1 5 2 0 9 2 0 0
2 8 7 7 0 2 2 2 5 4 0 3
'''